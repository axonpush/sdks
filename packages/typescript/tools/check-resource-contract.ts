/** Ensure facade request aliases match their generated operation types. */
import ts from "typescript";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const config = ts.readConfigFile(root + "/tsconfig.json", ts.sys.readFile).config;
const parsed = ts.parseJsonConfigFileContent(config, ts.sys, root);
const program = ts.createProgram(parsed.fileNames, parsed.options);
const checker = program.getTypeChecker();
let count = 0;
const issues: string[] = [];
for (const source of program.getSourceFiles()) {
  if (!source.fileName.startsWith(root + "/src/resources/")) continue;
  const visit = (node: ts.Node) => {
    if (
      ts.isCallExpression(node) &&
      ts.isPropertyAccessExpression(node.expression) &&
      node.expression.name.text === "invoke" &&
      node.arguments.length > 1
    ) {
      const op = node.arguments[0];
      const args = node.arguments[1];
      if (!op || !args) throw new Error("Resource operation arguments are missing");
      const sig = checker.getSignaturesOfType(
        checker.getTypeAtLocation(op),
        ts.SignatureKind.Call,
      )[0];
      const parameter = sig?.parameters[0];
      if (!parameter) throw new Error(`Cannot inspect operation ${op.getText()}`);
      const options = checker.getNonNullableType(checker.getTypeOfSymbolAtLocation(parameter, op));
      const actual = checker.getTypeAtLocation(args);
      for (const name of ["body", "query", "path"]) {
        const a = actual.getProperty(name);
        const e = options.getProperty(name);
        if (!a) continue;
        if (!e) {
          issues.push(`${source.fileName} ${op.getText()} unsupported ${name}`);
          continue;
        }
        const at = checker.getTypeOfSymbolAtLocation(a, args);
        const et = checker.getTypeOfSymbolAtLocation(e, op);
        count++;
        if (!checker.isTypeAssignableTo(at, et))
          issues.push(
            `${source.fileName} ${op.getText()} ${name}: ${checker.typeToString(at)} vs ${checker.typeToString(et)}`,
          );
      }
    }
    ts.forEachChild(node, visit);
  };
  visit(source);
}
console.log(`Audited ${count} operation request body/query/path aliases`);
for (const issue of issues) console.log(issue);
if (issues.length) process.exitCode = 1;

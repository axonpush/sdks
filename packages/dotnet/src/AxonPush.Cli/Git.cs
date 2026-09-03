using System.Diagnostics;

namespace AxonPush.Cli;

/// <summary>
/// Best-effort repository lineage, so a gate decision can name a commit.
/// Deliberately forgiving: a checkout without git is still a valid place to
/// run an evaluation.
/// </summary>
internal static class Git
{
    public static GitLineage Capture()
    {
        var commit = Run("rev-parse HEAD");
        if (string.IsNullOrEmpty(commit))
        {
            return new GitLineage();
        }

        var branch = Run("rev-parse --abbrev-ref HEAD");
        return new GitLineage
        {
            GitCommit = commit,
            GitBranch = branch is null or "HEAD" ? null : branch,
            GitDirty = !string.IsNullOrEmpty(Run("status --porcelain --untracked-files=normal")),
        };
    }

    private static string? Run(string arguments)
    {
        try
        {
            using var process = Process.Start(new ProcessStartInfo("git", arguments)
            {
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
            });
            if (process is null)
            {
                return null;
            }

            var output = process.StandardOutput.ReadToEnd().Trim();
            if (!process.WaitForExit(10_000))
            {
                process.Kill(entireProcessTree: true);
                return null;
            }

            return process.ExitCode == 0 && output.Length > 0 ? output : null;
        }
        catch (Exception exception) when (exception is not OutOfMemoryException)
        {
            return null;
        }
    }
}

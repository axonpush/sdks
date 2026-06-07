using System.Collections;
using System.Globalization;

namespace AxonPush.Otel.Internal;

/// <summary>
/// Mirrors the Python <c>_stringify_values</c> helper used by the axonpush-python OTel exporter.
/// Keeps primitives, recurses into dictionaries, materialises enumerables, and falls back to
/// <see cref="object.ToString"/> for arbitrary objects.
/// </summary>
internal static class AttributeValueCoercer
{
    public static object? Coerce(object? value)
    {
        if (value is null)
        {
            return null;
        }

        switch (value)
        {
            case string:
            case bool:
            case int:
            case long:
            case short:
            case byte:
            case sbyte:
            case uint:
            case ulong:
            case ushort:
            case double:
            case float:
            case decimal:
                return value;
        }

        if (value is IDictionary<string, object?> map)
        {
            var copy = new Dictionary<string, object?>(map.Count, StringComparer.Ordinal);
            foreach (var kvp in map)
            {
                copy[kvp.Key] = Coerce(kvp.Value);
            }
            return copy;
        }

        if (value is IDictionary nonGeneric)
        {
            var copy = new Dictionary<string, object?>(nonGeneric.Count, StringComparer.Ordinal);
            foreach (DictionaryEntry entry in nonGeneric)
            {
                copy[Convert.ToString(entry.Key, CultureInfo.InvariantCulture) ?? string.Empty] = Coerce(entry.Value);
            }
            return copy;
        }

        if (value is IEnumerable enumerable)
        {
            var list = new List<object?>();
            foreach (var item in enumerable)
            {
                list.Add(Coerce(item));
            }
            return list;
        }

        return Convert.ToString(value, CultureInfo.InvariantCulture);
    }
}

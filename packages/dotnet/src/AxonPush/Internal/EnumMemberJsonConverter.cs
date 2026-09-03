using System.Reflection;
using System.Runtime.Serialization;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace AxonPush.Internal;

/// <summary>
/// Serialises an enum using the wire value the contract declares.
///
/// NSwag records the wire value as <see cref="EnumMemberAttribute"/> but asks
/// System.Text.Json for <c>JsonStringEnumConverter</c>, which uses the .NET
/// member name instead — so `cli` went out as `Cli` and `agent.start` as
/// `Agent_start`. The generated file is rewritten to use this converter.
/// </summary>
internal sealed class EnumMemberJsonConverter<T> : JsonConverter<T>
    where T : struct, Enum
{
    private static readonly Dictionary<T, string> ToWire = typeof(T)
        .GetFields(BindingFlags.Public | BindingFlags.Static)
        .ToDictionary(
            field => (T)field.GetValue(null)!,
            field => field.GetCustomAttribute<EnumMemberAttribute>()?.Value ?? field.Name);

    private static readonly Dictionary<string, T> FromWire =
        ToWire.ToDictionary(entry => entry.Value, entry => entry.Key, StringComparer.OrdinalIgnoreCase);

    public override T Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        var value = reader.GetString();
        if (value is not null && FromWire.TryGetValue(value, out var parsed))
        {
            return parsed;
        }

        throw new JsonException($"'{value}' is not a value {typeof(T).Name} accepts.");
    }

    public override void Write(Utf8JsonWriter writer, T value, JsonSerializerOptions options)
    {
        writer.WriteStringValue(ToWire.TryGetValue(value, out var wire) ? wire : value.ToString());
    }
}

/// <summary>Serializer options shared by every generated API client.</summary>
internal static class AxonPushApiJson
{
    /// <summary>
    /// Unset optional fields are omitted rather than sent as null. The gate
    /// endpoint validates with `forbidNonWhitelisted` and reads thresholds with
    /// a null check, so a body full of nulls is noise at best.
    /// </summary>
    public static JsonSerializerOptions CreateOptions() =>
        new() { DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull };
}

# AUTO GENERATED FILE - DO NOT EDIT

export dashemojimart

"""
    dashemojimart(;kwargs...)

A DashEmojiMart component.

Keyword arguments:
- `id` (String; optional)
- `autoFocus` (Bool; optional)
- `categories` (Array; optional)
- `categoryIcons` (Dict; optional)
- `custom` (Array; optional)
- `dynamicWidth` (Bool; optional)
- `emojiButtonColors` (Array; optional)
- `emojiButtonRadius` (String; optional)
- `emojiButtonSize` (Real; optional)
- `emojiSize` (Real; optional)
- `emojiVersion` (Real; optional)
- `exceptEmojis` (Array; optional)
- `icons` (String; optional)
- `locale` (String; optional)
- `maxFrequentRows` (Real; optional)
- `navPosition` (String; optional)
- `noCountryFlags` (Bool; optional)
- `noResultsEmoji` (String; optional)
- `perLine` (Real; optional)
- `previewEmoji` (String; optional)
- `previewPosition` (String; optional)
- `searchPosition` (String; optional)
- `set` (String; optional)
- `skin` (Real; optional)
- `skinTonePosition` (String; optional)
- `theme` (String; optional)
- `value` (String; optional)
"""
function dashemojimart(; kwargs...)
        available_props = Symbol[:id, :autoFocus, :categories, :categoryIcons, :custom, :dynamicWidth, :emojiButtonColors, :emojiButtonRadius, :emojiButtonSize, :emojiSize, :emojiVersion, :exceptEmojis, :icons, :locale, :maxFrequentRows, :navPosition, :noCountryFlags, :noResultsEmoji, :perLine, :previewEmoji, :previewPosition, :searchPosition, :set, :skin, :skinTonePosition, :theme, :value]
        wild_props = Symbol[]
        return Component("dashemojimart", "DashEmojiMart", "dash_emoji_mart", available_props, wild_props; kwargs...)
end


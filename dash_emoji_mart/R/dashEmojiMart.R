# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashEmojiMart <- function(id=NULL, autoFocus=NULL, categoryIcons=NULL, custom=NULL, dynamicWidth=NULL, emojiButtonColors=NULL, emojiButtonRadius=NULL, emojiButtonSize=NULL, emojiSize=NULL, emojiVersion=NULL, exceptEmojis=NULL, getSpritesheetURL=NULL, icons=NULL, locale=NULL, maxFrequentRows=NULL, navPosition=NULL, noCountryFlags=NULL, noResultsEmoji=NULL, onAddCustomEmoji=NULL, onClickOutside=NULL, onEmojiSelect=NULL, perLine=NULL, previewEmoji=NULL, previewPosition=NULL, searchPosition=NULL, set=NULL, skin=NULL, skinTonePosition=NULL, theme=NULL, value=NULL) {
    
    props <- list(id=id, autoFocus=autoFocus, categoryIcons=categoryIcons, custom=custom, dynamicWidth=dynamicWidth, emojiButtonColors=emojiButtonColors, emojiButtonRadius=emojiButtonRadius, emojiButtonSize=emojiButtonSize, emojiSize=emojiSize, emojiVersion=emojiVersion, exceptEmojis=exceptEmojis, getSpritesheetURL=getSpritesheetURL, icons=icons, locale=locale, maxFrequentRows=maxFrequentRows, navPosition=navPosition, noCountryFlags=noCountryFlags, noResultsEmoji=noResultsEmoji, onAddCustomEmoji=onAddCustomEmoji, onClickOutside=onClickOutside, onEmojiSelect=onEmojiSelect, perLine=perLine, previewEmoji=previewEmoji, previewPosition=previewPosition, searchPosition=searchPosition, set=set, skin=skin, skinTonePosition=skinTonePosition, theme=theme, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashEmojiMart',
        namespace = 'dash_emoji_mart',
        propNames = c('id', 'autoFocus', 'categoryIcons', 'custom', 'dynamicWidth', 'emojiButtonColors', 'emojiButtonRadius', 'emojiButtonSize', 'emojiSize', 'emojiVersion', 'exceptEmojis', 'getSpritesheetURL', 'icons', 'locale', 'maxFrequentRows', 'navPosition', 'noCountryFlags', 'noResultsEmoji', 'onAddCustomEmoji', 'onClickOutside', 'onEmojiSelect', 'perLine', 'previewEmoji', 'previewPosition', 'searchPosition', 'set', 'skin', 'skinTonePosition', 'theme', 'value'),
        package = 'dashEmojiMart'
        )

    structure(component, class = c('dash_component', 'list'))
}

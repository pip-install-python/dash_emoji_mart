# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashEmojiMart(Component):
    """A DashEmojiMart component.


Keyword arguments:

- id (string; optional)

- autoFocus (boolean; default False)

- categoryIcons (dict; optional)

- custom (list; optional)

- dynamicWidth (boolean; default False)

- emojiButtonColors (list; optional)

- emojiButtonRadius (string; default "100%")

- emojiButtonSize (number; default 36)

- emojiSize (number; default 24)

- emojiVersion (number; default 14)

- exceptEmojis (list; optional)

- icons (string; default "auto")

- locale (string; default "en")

- maxFrequentRows (number; default 4)

- navPosition (string; default "top")

- noCountryFlags (boolean; default False)

- noResultsEmoji (string; default "cry")

- perLine (number; default 9)

- previewEmoji (string; default "point_up")

- previewPosition (string; default "bottom")

- searchPosition (string; default "sticky")

- set (string; default "native")

- skin (number; default 1)

- skinTonePosition (string; default "preview")

- theme (string; default "auto")

- value (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_emoji_mart'
    _type = 'DashEmojiMart'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, custom=Component.UNDEFINED, onEmojiSelect=Component.UNDEFINED, onClickOutside=Component.UNDEFINED, onAddCustomEmoji=Component.UNDEFINED, autoFocus=Component.UNDEFINED, categoryIcons=Component.UNDEFINED, dynamicWidth=Component.UNDEFINED, emojiButtonColors=Component.UNDEFINED, emojiButtonRadius=Component.UNDEFINED, emojiButtonSize=Component.UNDEFINED, emojiSize=Component.UNDEFINED, emojiVersion=Component.UNDEFINED, exceptEmojis=Component.UNDEFINED, icons=Component.UNDEFINED, locale=Component.UNDEFINED, maxFrequentRows=Component.UNDEFINED, navPosition=Component.UNDEFINED, noCountryFlags=Component.UNDEFINED, noResultsEmoji=Component.UNDEFINED, perLine=Component.UNDEFINED, previewEmoji=Component.UNDEFINED, previewPosition=Component.UNDEFINED, searchPosition=Component.UNDEFINED, set=Component.UNDEFINED, skin=Component.UNDEFINED, skinTonePosition=Component.UNDEFINED, theme=Component.UNDEFINED, getSpritesheetURL=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autoFocus', 'categoryIcons', 'custom', 'dynamicWidth', 'emojiButtonColors', 'emojiButtonRadius', 'emojiButtonSize', 'emojiSize', 'emojiVersion', 'exceptEmojis', 'icons', 'locale', 'maxFrequentRows', 'navPosition', 'noCountryFlags', 'noResultsEmoji', 'perLine', 'previewEmoji', 'previewPosition', 'searchPosition', 'set', 'skin', 'skinTonePosition', 'theme', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autoFocus', 'categoryIcons', 'custom', 'dynamicWidth', 'emojiButtonColors', 'emojiButtonRadius', 'emojiButtonSize', 'emojiSize', 'emojiVersion', 'exceptEmojis', 'icons', 'locale', 'maxFrequentRows', 'navPosition', 'noCountryFlags', 'noResultsEmoji', 'perLine', 'previewEmoji', 'previewPosition', 'searchPosition', 'set', 'skin', 'skinTonePosition', 'theme', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashEmojiMart, self).__init__(**args)

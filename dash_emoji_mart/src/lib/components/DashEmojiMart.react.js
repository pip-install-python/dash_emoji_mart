import React from 'react';
import PropTypes from 'prop-types';
import Picker from '@emoji-mart/react';
import data from '@emoji-mart/data';

const DashEmojiMart = (props) => {
    const {id, setProps, value, custom, onClickOutside, onAddCustomEmoji, autoFocus,  categories, categoryIcons, dynamicWidth, emojiButtonColors, emojiButtonRadius, emojiButtonSize, emojiSize, emojiVersion, exceptEmojis, icons, locale, maxFrequentRows, navPosition, noCountryFlags, noResultsEmoji, perLine, previewEmoji, previewPosition, searchPosition, set, skin, skinTonePosition, theme, getSpritesheetURL} = props;

    const handleEmojiSelect = (emoji) => {
        let emojiValue;
        // console.log("Test emoji:", emoji.src);
        if (emoji.src) {
            // console.log("Custom emoji:", emoji);
            emojiValue = emoji.src;
        } else {
            // console.log("Regular emoji:", emoji);
            emojiValue = emoji.native;
        }
        // console.log("Emoji value:", emojiValue);

        if (setProps) {
            setProps({ value: emojiValue });
        }
    };

    return (
        <div id={id}>
            <Picker
                data={data}
                // onSelect={handleEmojiSelect}
                emoji={value}
                custom={custom}
                onEmojiSelect={handleEmojiSelect}
                onClickOutside={onClickOutside}
                onAddCustomEmoji={onAddCustomEmoji}
                autoFocus={autoFocus}
                categories={categories}
                categoryIcons={categoryIcons}
                dynamicWidth={dynamicWidth}
                emojiButtonColors={emojiButtonColors}
                emojiButtonRadius={emojiButtonRadius}
                emojiButtonSize={emojiButtonSize}
                emojiSize={emojiSize}
                emojiVersion={emojiVersion}
                exceptEmojis={exceptEmojis}
                icons={icons}
                locale={locale}
                maxFrequentRows={maxFrequentRows}
                navPosition={navPosition}
                noCountryFlags={noCountryFlags}
                noResultsEmoji={noResultsEmoji}
                perLine={perLine}
                previewEmoji={previewEmoji}
                previewPosition={previewPosition}
                searchPosition={searchPosition}
                set={set}
                skin={skin}
                skinTonePosition={skinTonePosition}
                theme={theme}
                getSpritesheetURL={getSpritesheetURL}
            />
        </div>
    );
}

DashEmojiMart.defaultProps = {
    custom: [],
    onEmojiSelect: null,
    onClickOutside: null,
    onAddCustomEmoji: null,
    autoFocus: false,
    categories: [],
    categoryIcons: {},
    dynamicWidth: false,
    emojiButtonColors: [],
    emojiButtonRadius: "100%",
    emojiButtonSize: 36,
    emojiSize: 24,
    emojiVersion: 14,
    exceptEmojis: [],
    icons: "auto",
    locale: "en",
    maxFrequentRows: 4,
    navPosition: "top",
    noCountryFlags: false,
    noResultsEmoji: "cry",
    perLine: 9,
    previewEmoji: "point_up",
    previewPosition: "bottom",
    searchPosition: "sticky",
    set: "native",
    skin: 1,
    skinTonePosition: "preview",
    theme: "auto",
    getSpritesheetURL: null
};

DashEmojiMart.propTypes = {
    id: PropTypes.string,
    value: PropTypes.string,
    setProps: PropTypes.func,
    custom: PropTypes.array,
    onEmojiSelect: PropTypes.func,
    onClickOutside: PropTypes.func,
    onAddCustomEmoji: PropTypes.func,
    autoFocus: PropTypes.bool,
    categories: PropTypes.array,
    categoryIcons: PropTypes.object,
    dynamicWidth: PropTypes.bool,
    emojiButtonColors: PropTypes.array,
    emojiButtonRadius: PropTypes.string,
    emojiButtonSize: PropTypes.number,
    emojiSize: PropTypes.number,
    emojiVersion: PropTypes.number,
    exceptEmojis: PropTypes.array,
    icons: PropTypes.string,
    locale: PropTypes.string,
    maxFrequentRows: PropTypes.number,
    navPosition: PropTypes.string,
    noCountryFlags: PropTypes.bool,
    noResultsEmoji: PropTypes.string,
    perLine: PropTypes.number,
    previewEmoji: PropTypes.string,
    previewPosition: PropTypes.string,
    searchPosition: PropTypes.string,
    set: PropTypes.string,
    skin: PropTypes.number,
    skinTonePosition: PropTypes.string,
    theme: PropTypes.string,
    getSpritesheetURL: PropTypes.func
};

export default DashEmojiMart;

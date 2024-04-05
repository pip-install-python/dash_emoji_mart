from dash_emoji_mart import DashEmojiMart
from dash import Dash, callback, html, Input, Output
from urllib.parse import urlparse

app = Dash(__name__)

custom=[
    {
        'id': 'gifs',
        'name': 'GIFs',
        'emojis': [
            {
                'id': 'party_parrot',
                'name': 'Party Parrot',
                'short_names': ['party_parrot'],
                'keywords': ['dance', 'dancing'],
                'skins': [{'src': 'https://missiveapp.com/open/emoji-mart/parrot.6a845cb2.gif'}],
                'native': '',
                'unified': 'gifs',
            },
            {
                'id': 'plotly',
                'name': 'Plotly',
                'short_names': ['plotly'],
                'keywords': ['plotly', 'dash'],
                'skins': [{'src': 'https://store-images.s-microsoft.com/image/apps.36868.bfb0e2ee-be9e-4c73-807f-e0a7b805b1be.712aff5d-5800-47e0-97be-58d17ada3fb8.a46845e6-ce94-44cf-892b-54637c6fcf06'}],
                'native': '',
                'unified': 'gifs',
            },
        ],
    },
]

app.layout = html.Div([
   DashEmojiMart(
       id='input',
       custom=custom,
       autoFocus=False,
       categoryIcons={},
       dynamicWidth=False,
       emojiButtonColors=[],
       emojiButtonRadius="100%",
       emojiButtonSize=36,
       emojiSize=24,
       emojiVersion=14,
       exceptEmojis=[],
       icons="auto",
       locale="en",
       maxFrequentRows=4,
       navPosition="top",
       noCountryFlags=False,
       noResultsEmoji="cry",
       perLine=9,
       previewEmoji="point_up",
       previewPosition="bottom",
       searchPosition="sticky",
       set="native",
       skin=1,
       skinTonePosition="preview",
       theme="auto",
    ),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    Input('input', 'value')
)
def update_output(value):
    print(value)
    # Check if value is a URL
    try:
        result = urlparse(value)
        if all([result.scheme, result.netloc]):
            # If value is a URL, return it as an image
            return html.Img(src=value, style={'width': '40px'})
    except ValueError:
        pass
    # If value is not a URL, return it as is
    return html.H1(value)

if __name__ == '__main__':
    app.run_server(debug=True, port='1111')
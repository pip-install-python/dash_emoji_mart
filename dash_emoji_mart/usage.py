from dash import *
from dash_emoji_mart import DashEmojiMart
from urllib.parse import urlparse

app = Dash(__name__)

custom = [
    {
        'id': 'custom',
        'name': 'Custom',
        'emojis': [
            {
                'id': 'party_parrot',
                'name': 'Party Parrot',
                'short_names': ['party_parrot'],
                'keywords': ['dance', 'dancing'],
                'skins': [{'src': 'https://missiveapp.com/open/emoji-mart/parrot.6a845cb2.gif'}],
                'native': '',
                'unified': 'custom',
            },
            {
                'id': 'plotly',
                'name': 'Plotly',
                'short_names': ['plotly'],
                'keywords': ['plotly', 'dash'],
                'skins': [{'src': 'https://store-images.s-microsoft.com/image/apps.36868.bfb0e2ee-be9e-4c73-807f-e0a7b805b1be.712aff5d-5800-47e0-97be-58d17ada3fb8.a46845e6-ce94-44cf-892b-54637c6fcf06'}],
                'native': '',
                'unified': 'custom',
            },
        ],
    },
]

app.layout = html.Div([
   DashEmojiMart(
       id='input',
       custom=custom,
       autoFocus=False,
       categories=['activity', 'custom'],
       categoryIcons={'activity': {'svg': '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path d="M57.89 397.2c-6.262-8.616-16.02-13.19-25.92-13.19c-23.33 0-31.98 20.68-31.98 32.03c0 6.522 1.987 13.1 6.115 18.78l46.52 64C58.89 507.4 68.64 512 78.55 512c23.29 0 31.97-20.66 31.97-32.03c0-6.522-1.988-13.1-6.115-18.78L57.89 397.2zM496.1 352c-44.13 0-79.72 35.75-79.72 80s35.59 80 79.72 80s79.91-35.75 79.91-80S540.2 352 496.1 352zM640 99.38c0-13.61-4.133-27.34-12.72-39.2l-23.63-32.5c-13.44-18.5-33.77-27.68-54.12-27.68c-13.89 0-27.79 4.281-39.51 12.8L307.8 159.7C262.2 192.8 220.4 230.9 183.4 273.4c-24.22 27.88-59.18 63.99-103.5 99.63l56.34 77.52c53.79-35.39 99.15-55.3 127.1-67.27c51.88-22 101.3-49.87 146.9-82.1l202.3-146.7C630.5 140.4 640 120 640 99.38z"/></svg>', 'people': 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fpreviews%2F000%2F379%2F228%2Foriginal%2Fcool-emoji-vector-icon.jpg'}, 'custom': {'svg': '<svg xmlns="http://www.w3.org/2000/svg" width="0.92em" height="1em" viewBox="0 0 256 280"><path fill="#991b21" d="M70.882 129.428s-3.212-.666-4.155-.381c-.943.285-6.33-.66-8.693-2.37c-2.364-1.703-4.725-.47-6.897-1.8c-2.17-1.328-5.48-1.139-7.933-1.232c-2.456-.093-5.575.093-6.71 1.61c-1.133 1.516-5.571 6.164-7.177 8.057c-1.606 1.896-8.124 8.719-10.675 9.76c0 0 .66 1.046.283 1.802c-.379.762-.095 2.937-.095 3.698c0 .762.188 1.989-.469 2.75c-.665.76-1.041 1.99-1.041 2.463c0 .474-.758 2.18 0 4.457c.755 2.276 1.414 4.832-1.702 3.791c-3.118-1.04-2.456-3.884-5.005-3.983c-2.548-.093-5.855 0-6.801-3.503c-.949-3.51-2.74-9.48-3.119-10.429c-.376-.945-1.698-5.306.758-9.097c2.456-3.79 2.928-6.541 3.307-7.396c.376-.852 2.173-6.256 3.492-7.018c1.322-.759.848-3.128 1.606-4.169c.755-1.043.471-2.75.943-3.698c.471-.948.662-3.695 1.322-5.78c.662-2.084 2.835-5.311 4.157-7.015c1.322-1.704 2.08-4.262 2.08-5.117c0-.854-.471-2.651 1.698-4.169c2.17-1.517 6.044-6.445 6.423-7.204c0-.189 0-3.695-.19-4.928c-.189-1.233-.472-2.37.754-2.843c1.233-.477 2.93-1.52 2.93-1.52s-1.178-1.515-3.73-2.796C23.692 70.09 16.04 61.416 15.333 56.3c-.711-5.12-.995-13.224 5.95-16.067c6.945-2.847 14.594-4.41 15.731-4.55c1.134-.141 5.1-.996 6.661.14c0 0-1.7-.281-2.408 0c-.71.286 3.396.145 4.39 1.281c0 0-1.982-.567-3.116-.426c-1.131.141 1.985 1.422 2.552 2.418c.564.995 2.692 1.706 2.408 3.272c-.28 1.563-.424 3.98-.143 4.69c.287.712.994 1.992 1.137 3.98c.143 1.992.71 4.695 1.274 5.972c.568 1.281 1.985 5.261 1.418 8.104c0 0 .567 1.422 3.4-1.847c2.835-3.272 5.67-3.84 7.085-3.84c1.417 0 3.545-1.424 4.96-.854c1.42.57 2.98-.14 4.68.285c1.697.426 8.782 0 10.343-.57c1.555-.57 6.942-1.28 8.073-1.28c1.134 0-1.414-1.848.71-3.27c2.128-1.421-2.268-2.132.994-6.253c3.256-4.124.138-5.261-.426-6.113c-.565-.855-.708-3.557-.708-5.12c0-1.565-.424-5.545-.424-5.545l.567-.711s-.457-.756-.906-1.024c-.447-.268-.893-1.881-1.247-2.956c-.362-1.075-4.289-6.9-5.448-7.794c-1.162-.9-1.34-2.24-1.162-3.495c.18-1.258 1.07-2.33.892-3.675c-.18-1.343-.09-3.134-.18-3.76c-.086-.63.18-4.39.986-4.748c0 0 .623-.27.893.624c0 0-.45-3.134.533-3.134c0 0 1.162-.358 1.608 1.255c.444 1.614.893 2.508.983 2.956c.09.449.446 1.162.446 1.162s.98-.442 1.786-.087c.802.358 1.341.716 1.341 1.165c0 .448 0-.358.983-.358c.98 0 1.875-.271 2.144.716c.264.985.447 1.704.534 2.688c.092.985.27 1.792.626 2.508c.359.717.89 1.969.89 3.673c0 1.703.628 4.837.895 6.273c.267 1.433 3.304 6.987 3.304 6.987s4.643.897 6.785.449c2.144-.449 5.892.358 5.448 2.33c-.446 1.968-.713 7.793-.892 12.363c-.18 4.57-.896 13.438-1.609 16.575c-.716 3.134-5.09 11.288-6.874 12.631c-1.783 1.346-3.75 2.24-8.66 4.57a849.844 849.844 0 0 1-10.628 4.928s3.037 4.298 3.75 4.57c.713.267.626-.627 1.516-.272c.444.178 1.985.785 1.005.381c-.002.038 5.38 1.42 5.38 1.42c.515-.01.834-.104.77-.41c-.27-1.251.983-2.863 1.516-3.224c.537-.358-.803 1.612 0 2.506c.806.899 12.348-2.531 12.132-1.917c-.213.615.626.662 1.362.085c.73-.575 3.788-2.574 5.968-2.565c2.185.01 7.127.448 8.453-.037c1.325-.482 7.352-4.214 9.365-5.2c2.008-.993 8.948-.897 11.877-2.876c2.929-1.981 9.38-6.618 12.103-8.306c2.722-1.686 22.916-14.077 27.224-14.75c4.308-.674 14.634-4.761 16.403-6.027c1.77-1.263 7.335-4.338 8.45-5.302c1.118-.964 6.701 1.486 9.61 5.638c0 0 5.676-2.788 6.9-2.895c1.222-.107 3.485-1.689 5.221-3.022c1.738-1.336 6.973-4.873 9.262-5.992c0 0 1.157-.51 1.379-1.325c.221-.815 1.145-2.37 1.977-2.05c0 0 1.822-2.333 2.56-1.631c0 0 1.602-1.52 2.52-.694c0 0 .907.13 1.213.62c0 0 1.151-.933 1.685-.225c0 0 .831-.942 2.233.163c0 0 .932 1.153-.784 3.273c0 0-1.075.558-1.828 2.114c-.747 1.556-2.84 4.513-5.13 5.671c-2.298 1.159-4.95 3.194-4.85 7.354c.1 4.163-1.666 9.003-6.022 7.915c-4.355-1.088-8.175.38-11.988 2.463c0 0-.335 2.2-.702 2.723c-.371.522-2.076.353-4.42 1.827c-2.343 1.471-3.772 2.024-5.62 3.41c-1.85 1.387-2.247 2.323-3.803 3.047c-1.555.73-3.302 2.71-4.333 3.806c-1.036 1.093-4.847 3.785-9.351 5.984c-4.508 2.201-23.034 8.834-27.317 12.32c-4.288 3.487-12.17 9.733-24.134 15.607c-.497.243-.958.48-1.427.713c-.724.663-11.011 10.105-14.533 12.575c-3.65 2.559-5.11 2.925-6.206 8.78c-.719 3.859-3.654 10.088-5.681 15.049a243.782 243.782 0 0 0-.812 12.377c-.14 3.695-4.855 40.442-5.99 44.416c-1.137 3.98-1.418 6.965-.85 10.091c.566 3.12-.852 6.816-2.55 9.942c-1.705 3.126-4.539 10.514-4.115 14.775c.424 4.262.851 5.827-.424 6.393c-1.278.567-5.39.429-5.954 1.85c-.567 1.42-2.693 1.42-2.693 1.42s-.637 6.34.475 7.455c1.115 1.11 5.046 5.781.264 9.26c-4.788 3.484-9.835 6.573-11.011 9.005c-1.183 2.427-3.806 3.811-4.789 4.598c-.982.786-2.752 1.905-2.884 2.362c-.129.462-1.57 1.316-2.948.924c0 0-1.18.522-2.427-.86c0 0-2.027.198-2.423-1.113c0 0-1.705.127-1.902-1.184c0 0-.853-1.905 1.705-2.691c2.553-.793 6.62-6.509 6.751-7.428c.13-.919 2.033-6.638 3.474-9c1.44-2.367 3.342-8.543 3.606-14.192c0 0-.587-.392-.587-.98c0-.596.034-3.31.317-4.35c.287-1.046.851-4.073.475-8.527c-.38-4.447.567-11.742 0-16.762s.511-39.87 2.022-44.417c1.514-4.547 2.078-5.587 1.985-7.388c-.095-1.801 0-7.295.568-7.577c.564-.284.66-7.198.471-7.96c-.19-.755-4.254-3.596-4.819-5.586c0 0 .093 2.083 0 2.841c-.095.758-.188-.189-1.701-1.801c-1.517-1.612-4.35-5.02-4.539-7.484c-.338-.183-4.525-2.656-4.525-2.656c-.52.023-.78-.223-.905-.437"/><path d="M90.196 87.431c-.428 7.693-18.42 42.734-18.42 42.734c-.628 3.1-.498 5.995-.18 7.716c.762 4.126-3.05 10.316-3.05 10.316l4.151 2.185c5.607-3.25 3.203-12.999 3.203-12.999a12.21 12.21 0 0 1-.27-5l.045.046S96.078 91.987 95.09 88.802c-.002.006-2.434-.345-4.894-1.37"/></svg>'},
                      'custom': {'svg': '<svg xmlns="http://www.w3.org/2000/svg" width="0.9em" height="1em" viewBox="0 0 256 286"><path fill="#555" d="M246.716 95.492c-6.899-8.36-16.64-13.533-27.428-14.566c-10.79-1.035-21.335 2.197-29.695 9.095a40.467 40.467 0 0 0-10.383 12.96l-9.798-3.877c2.65-3.818 6.124-7.813 10.101-11.516c8.243-7.677 17.296-12.846 24.84-14.183c.501-.09.945-.38 1.226-.806c.503-.761 1.295-1.631 1.994-2.399c1.527-1.677 2.97-3.26 1.587-4.822a1.859 1.859 0 0 0-1.504-.624c-13.097.798-31.694 6.942-44.612 21.793c-2.365 2.72-4.382 5.231-6.087 7.629L118.79 79.072c-2.16-2.774-5.193-4.886-6.985-5.045c-.289-.028-.669.068-1.109.247c.938-2.355 1.86-5.157 2.468-8.525c1.135-6.28 1.284-11.546 3.085-11.96c3.328-.765 2.967.936 3.633-1.498c.994-3.628-3.753-7.925-2.368-11.047c1.022-2.304 2.025-3.969 2.93-5.214c3.368.642 6.327 1.178 9.217 3.068c3.039-2.815 5.578-7.006 5.011-10.16c-.583-3.25-6.866-3.094-5.57-8.94c.851-3.842 6.28-5.01 9.72-4.939c1.908.037 1.286-8.225-.992-9.536c-2.875-1.653-28.095-10.405-36.599-1.786c-4.755 4.82-7.037 17.652-1.607 22.301c.618.529 1.22 1.017 1.815 1.488c-.775.458-1.622.845-2.962.98c-2.953.297-4.594-.994-5.87.051c-1.293 1.06.928 2.372-.07 4.098c-1.826 3.156-3.506-1.163-9.501 4.77c-2.786 2.758-3.483 8.038-6.236 14.653c-4.423 10.629-8.302 8.584-13.394 24.955c-1.248 4.01 4.076 2.04 13.951 6.876c-4.814 9.116-7.933 17.75-6.46 23.152c1.813 6.649 14.69 17.015 21.371 22.921c.45.397.929.904 1.434 1.492C75.313 149.37 43.275 162.524.53 194.46c-2.014 3.252 2.225 8.644 4.114 9.021c25.15-21.219 55.4-28.04 86.691-25.796a491.496 491.496 0 0 1-10.724 6.506l1.576-4.027l-10.742 3.323l-49.651 15.615l-5.925 6.837l2.85 7.992l8.914 1.545l48.297-19.314l.459-1.173c15.614-4.419 18.506-.287 20.24 4.458l-7.657 8.169c-13.27-5.18-28.891-3.23-40.637 6.463c-17.257 14.24-19.712 39.866-5.472 57.122c8.013 9.71 19.63 14.733 31.333 14.733c9.095 0 18.243-3.035 25.79-9.263c8.36-6.897 13.533-16.638 14.567-27.428c.906-9.462-1.468-18.736-6.72-26.514l12.816-15.536c.582.175 1.123.232 1.616.153c1.824-.293 4.535-2.335 7.634-5.389c.597 1.13 1.804 1.849 3.12 1.724c1.76-.166 3.048-1.773 2.877-3.59a3.356 3.356 0 0 0-.643-1.672c5.807.902 10.524 1.093 10.913-.226c1.602-5.412-1.407-7.748-5.046-9.335a184.89 184.89 0 0 0 5.781-8.05c6.433-6.027 11.193-11.626 11.953-15.054c1.583-7.136-4.381-18.35-10.09-24.8c.415-4.287.917-9.205 1.397-14.104c.794 3.731 2.416 8.394 4.131 13.297c.999 2.855 2.031 5.807 2.884 8.554a1.858 1.858 0 0 0 3.247.583c.324-.422.723-.766 1.144-1.13c1.19-1.027 2.988-2.58 1.78-5.864c-5.2-14.149-1.259-26.205.635-31.999c.235-.718.437-1.337.6-1.885c.083-.278.182-.565.282-.852l11.166 3.981a41.157 41.157 0 0 0-1.004 5.91c-1.033 10.79 2.198 21.335 9.096 29.695s16.638 13.533 27.427 14.566a41.43 41.43 0 0 0 3.942.19c9.393 0 18.416-3.23 25.753-9.285c8.36-6.898 13.533-16.639 14.567-27.428c1.033-10.79-2.197-21.335-9.095-29.695zm-125.195 5.802c-4.583 1.607-8.715 3.808-11.544 6.606c-3.898-3.782-6.946-6.559-7.773-8.054a1.6 1.6 0 0 0 .85-.294c1.31-.957.145-3.288 1.818-4.575c2.736-2.107 7.584 2.796 10.737.856c1.432-.88 2.24-3.006 2.234-5.039l8.025 2.861zm-33.442 85.66a452.93 452.93 0 0 0 9.59-5.939a236.443 236.443 0 0 0 6.904 9.959l-3.36 3.585c-2.144-4.097-5.701-7.416-13.134-7.606zm18.096 21.31c.351-.053.713-.122 1.093-.216c2.18-.544 5.174-1.935 8.627-3.904c.166.146.33.29.494.427l-11.66 14.138a40.582 40.582 0 0 0-4.253-4.21zm-9.316 18.383c.222.27.433.546.644.82L85.682 241.8a12.017 12.017 0 0 0-2.215-4.103a12.045 12.045 0 0 0-2.273-2.11l11.752-12.853a29.421 29.421 0 0 1 3.913 3.913m6.595 21.534c-.75 7.825-4.5 14.889-10.563 19.891c-12.516 10.328-31.099 8.547-41.425-3.967c-10.327-12.515-8.546-31.098 3.968-41.426a29.284 29.284 0 0 1 18.703-6.716c2.139 0 4.274.233 6.365.692l-17.82 19.011l1.808 2.519c-3.239 4.351-3.24 10.498.368 14.87c4.24 5.138 11.844 5.866 16.983 1.626a12 12 0 0 0 3.41-4.569l15.053-18.25c2.587 4.98 3.698 10.6 3.15 16.32zm141.259-124.058c-.75 7.824-4.5 14.888-10.563 19.891c-6.063 5.003-13.707 7.344-21.535 6.596c-7.824-.75-14.888-4.501-19.89-10.564c-5.003-6.062-7.345-13.71-6.596-21.534c.104-1.083.271-2.15.488-3.2l16.742 5.97a12.015 12.015 0 0 0 2.758 7.714c4.24 5.139 11.844 5.867 16.983 1.627c5.138-4.24 5.867-11.844 1.626-16.983c-4.24-5.139-11.844-5.867-16.983-1.627c-.6.496-1.135 1.041-1.614 1.62l-16.485-6.523a29.393 29.393 0 0 1 7.05-8.488c5.32-4.392 11.863-6.733 18.675-6.733c.948 0 1.902.047 2.859.137c7.824.75 14.887 4.501 19.89 10.563c5.002 6.063 7.345 13.71 6.595 21.535z"/></svg>'}},
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
       theme="light",
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
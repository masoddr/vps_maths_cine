"""
Constantes pour les cinémas de Toulouse
Format:
    'CODE_CINEMA': {
        'id': 'ID_ALLOCINE',  # ID utilisé par Allociné
        'name': 'Nom Affiché'  # Nom qui sera affiché sur le site
    }
"""

from .tarifs import TARIFS_CINEMA

CINEMAS = {
    'ABC': {
        'id': 'P0071',
        'name': 'ABC'
    },
    'AMERICAN_COSMOGRAPH': {
        'id': 'P0235',
        'name': 'American Cosmograph'
    },
    'UTOPIA_BORDEROUGE': {
        'id': 'W3120',
        'name': 'Utopia Borderouge'
    },
    'CRATERE': {
        'id': 'P0056',
        'name': 'Le cratère'
    },
    'PATHE_WILSON': { #TODO: problème avec le pathé wilson 
        'id': 'P0057',
        'name': 'Pathé Wilson'
    },
    'UGC_MONTAUDRAN': {
        'id': 'W3140',
        'name': 'UGC Montaudran'
    }
}

def create_tarifs_modal(cinema_id):
    tarifs = TARIFS_CINEMA.get(cinema_id, {})
    
    modal = html.Div([
        html.Div([
            html.Button("×", 
                id=f"close-modal-{cinema_id}",
                className="modal-close-button",
                n_clicks=0
            ),
            html.H3("Tarifs", className="modal-title"),
            html.Div([
                render_tarifs_content(tarifs)
            ], className="modal-content")
        ], className="modal-container")
    ], id=f"modal-{cinema_id}", className="modal", style={"display": "none"})
    
    return modal

def render_tarifs_content(tarifs):
    content = []
    
    if "normal" in tarifs:
        content.append(html.P([
            html.Strong("Tarif normal : "),
            f"{tarifs['normal']}€"
        ]))
    
    if "carnet" in tarifs:
        carnet = tarifs["carnet"]
        content.append(html.P([
            html.Strong("Carnet : "),
            f"{carnet['prix']}€ ({carnet['nombre_places']} places)",
            html.Br(),
            html.Em(carnet['description'])
        ]))
    
    if "reduit" in tarifs:
        reduit = tarifs["reduit"]
        content.append(html.P([
            html.Strong("Tarif réduit : "),
            f"{reduit['prix']}€",
            html.Br(),
            html.Em("Conditions : "),
            html.Ul([
                html.Li(condition) for condition in reduit['conditions']
            ])
        ]))
    
    for key, value in tarifs.items():
        if key not in ["normal", "carnet", "reduit"]:
            if isinstance(value, (int, float)):
                content.append(html.P([
                    html.Strong(f"{key.replace('_', ' ').title()} : "),
                    f"{value}€"
                ]))
    
    return content

def create_cinema_card(cinema):
    return html.Div([
        // ... existing code ...
        html.Button(
            "Voir les tarifs",
            id=f"tarifs-button-{cinema['id']}",
            className="tarifs-button",
            n_clicks=0
        ),
        create_tarifs_modal(cinema['id'])
    ], className="cinema-card")

# Ajoutez ce style CSS
app.css.append_css({
    "external_url": "assets/modal.css"
})

@app.callback(
    [Output(f"modal-{cinema_id}", "style") for cinema_id in TARIFS_CINEMA.keys()],
    [Input(f"tarifs-button-{cinema_id}", "n_clicks") for cinema_id in TARIFS_CINEMA.keys()] +
    [Input(f"close-modal-{cinema_id}", "n_clicks") for cinema_id in TARIFS_CINEMA.keys()] +
    [Input(f"modal-{cinema_id}", "n_clicks") for cinema_id in TARIFS_CINEMA.keys()],
    prevent_initial_call=True
)
def toggle_modal(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        return [{"display": "none"}] * len(TARIFS_CINEMA)
    
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    cinema_id = button_id.split("-")[-1]
    
    outputs = [{"display": "none"}] * len(TARIFS_CINEMA)
    
    if "tarifs-button" in button_id:
        index = list(TARIFS_CINEMA.keys()).index(cinema_id)
        outputs[index] = {"display": "block"}
    
    return outputs 
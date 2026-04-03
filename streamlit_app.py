from __future__ import annotations

from pathlib import Path

import streamlit as st


# =========================================================
# CONFIGURACIÓN PERSONALIZADA
# =========================================================
APP = {
    "titulo": "La Champions de nuestros recuerdos",
    "subtitulo": "Un juego para ti, mi amor",
    "nombre": "Ismael",
    "firma": "De tu cachetona 💙",
    "frase_portada": "Bienvenido al torneo más bonito: el de nuestra historia.",
    "frase_final": "No necesito copa ni trofeo, contigo ya gané.",
    "colores": {
        "azul": "#2B6CB0",
        "verde_agua": "#67E8F9",
        "verde_jade": "#14B8A6",
        "oscuro": "#0F172A",
        "claro": "#F8FAFC",
        "dorado": "#F6C453",
        "borde": "#D9E2EC",
    },
}

OPTIONAL_HERO_IMAGES = [
    "assets/futbol_04.jpg",
]

TRIVIA = [
    {
        "pregunta": "¿Cuál es mi postre favorito?",
        "opciones": ["Pie de limón", "Tres leches", "Alfajores", "Cheesecake"],
        "correcta": 0,
        "explicacion": "Sí, mi postre favorito es el pie de limón.",
    },
    {
        "pregunta": "¿Qué es lo que más me pone triste?",
        "opciones": [
            "Que me ignores o me grites",
            "Que llegues temprano",
            "Que me compres flores",
            "Que me escribas mucho",
        ],
        "correcta": 0,
        "explicacion": "Eso sí me pone triste o molesta, porque necesito sentir amor y atención.",
    },
    {
        "pregunta": "¿Qué recuerdo digo siempre que es de mis favoritos?",
        "opciones": [
            "Cuando fuimos al cine",
            "Cuando me hiciste una canción entera",
            "Cuando fuimos al centro comercial",
            "Cuando salimos a caminar",
        ],
        "correcta": 1,
        "explicacion": "La canción entera tiene un lugar demasiado especial en mi corazón.",
    },
    {
        "pregunta": "¿Qué apodo me dices tú con cariño?",
        "opciones": ["Gordita", "Cachetona", "Princesa", "Amor"],
        "correcta": 1,
        "explicacion": "Sí, tú me dices cachetona 💙",
    },
    {
        "pregunta": "¿Qué plan representa mejor nuestra parte creativa?",
        "opciones": [
            "Pintar una foto nuestra",
            "Hacer postres",
            "Jugar ludo",
            "Ir de compras",
        ],
        "correcta": 0,
        "explicacion": "Nuestros momentos creativos también son parte de lo más bonito de nosotros.",
    },
    {
        "pregunta": "¿Dónde colocamos un candado juntos?",
        "opciones": ["En Barranco", "En el Parque del Amor", "En la playa", "En Lunahuaná"],
        "correcta": 1,
        "explicacion": "Ese recuerdo en Miraflores merece su propia copa.",
    },
]

PHOTO_ROUNDS = [
    {
        "label": "Foto 1: circuito mágico del agua",
        "path": "assets/foto_circuito.jpg",
        "pregunta": "¿Qué recuerdo fue este?",
        "opciones": ["Circuito Mágico del Agua", "Parque del Amor", "Lunahuaná", "Mandrake"],
        "correcta": 0,
        "explicacion": "Ese fue uno de los primeros recuerdos más bonitos de nosotros.",
    },
    {
        "label": "Foto 2: Miraflores",
        "path": "assets/foto_miraflores.jpg",
        "pregunta": "¿Qué pasó en este recuerdo?",
        "opciones": [
            "Pusimos un candado en el Parque del Amor",
            "Fuimos a comer un postre",
            "Paseo en Miraflores",
            "Fuimos a la playa",
        ],
        "correcta": 2,
        "explicacion": "Ese recuerdo es de nuestras primeras citas.",
    },
    {
        "label": "Foto 3: playa",
        "path": "assets/foto_playa.png",
        "pregunta": "¿Qué hicimos ese día?",
        "opciones": [
            "Fuimos a ver el atardecer",
            "Fuimos a tirar el candado",
            "Jugamos fútbol",
            "Fuimos a almorzar",
        ],
        "correcta": 1,
        "explicacion": "Hasta nuestros planes más locos se volvieron hermosos juntos.",
    },
    {
        "label": "Foto 4: anillo de promesa",
        "path": "assets/foto_anillo.jpg",
        "pregunta": "¿Qué representa este momento?",
        "opciones": [
            "Fuimos a comer waffles",
            "Nuestro anillo de promesa",
            "Una salida de improviso",
            "Un cumpleaños diferente",
        ],
        "correcta": 1,
        "explicacion": "Ese momento también quedó guardado en mi corazón.",
    },
]

# =========================================================
# CRUCIGRAMA — cada pista es una palabra de la frase secreta.
# Al completarlas todas bien, la frase se revela.
# =========================================================
CROSSWORD = [
    {"num": 1,  "pista": "Palabra de negación. (2 letras)",                                               "respuesta": "NO"},
    {"num": 2,  "pista": "Verbo que usas cuando conoces algo. (2 letras)",                                "respuesta": "SE"},
    {"num": 3,  "pista": "Lo contrario de 'poco'. (5 letras)",                                            "respuesta": "MUCHO"},
    {"num": 4,  "pista": "Palabra pequeña que sirve para relacionar ideas. (2 letras)",                   "respuesta": "DE"},
    {"num": 5,  "pista": "Deporte que tanto te gusta jugar. (7 letras)",                                  "respuesta": "FUTBOL"},
    {"num": 6,  "pista": "Palabra que se usa para contradecir o cambiar una idea. (4 letras)",            "respuesta": "PERO"},
    {"num": 7,  "pista": "Afirmación, lo contrario de 'no'. (2 letras)",                                  "respuesta": "SI"},
    {"num": 8,  "pista": "Otra vez, verbo de saber o conocer. (2 letras)",                                "respuesta": "SE"},
    {"num": 9,  "pista": "Palabra muy común para unir una idea con otra. (3 letras)",                     "respuesta": "QUE"},
    {"num": 10, "pista": "Pronombre que habla de mí. (2 letras)",                                         "respuesta": "ME"},
    {"num": 11, "pista": "Un verbo para decir que algo te gusta muchísimo. (7 letras)",                   "respuesta": "ENCANTA"},
    {"num": 12, "pista": "Mirarte a ti. (5 letras)",                                                      "respuesta": "VERTE"},
    {"num": 13, "pista": "Destacar, lucirte, llamar la atención por lo bien que haces algo. (7 letras)", "respuesta": "BRILLAR"},
]

TIMELINE = [
    "Circuito Mágico del Agua",
    "Miraflores y el candado en el Parque del Amor",
    "La playa para tirar el candado",
    "El anillo de promesa",
    "Fukk Day en Lunahuaná",
    "Almuerzo en Mandrake, Miraflores",
]
TIMELINE_ITEMS = [
    {
        "id": "circuito",
        "label": "Circuito Mágico del Agua",
        "path": "assets/foto_circuito.jpg",
    },
    {
        "id": "parque",
        "label": "Parque del Amor",
        "path": "assets/foto_parque.jpg",
    },
    {
        "id": "miraflores",
        "label": "Candado en el Parque del Amor",
        "path": "assets/foto_candado.jpg",
    },
    {
        "id": "playa",
        "label": "La playa para tirar el candado",
        "path": "assets/foto_playa.png",
    },
    {
        "id": "lunahuaná",
        "label": "Full Day en Lunahuaná",
        "path": "assets/foto_lunahuana.jpg",
    },
    {
        "id": "mandrake",
        "label": "Almuerzo en Mandrake",
        "path": "assets/foto_mandrake.jpeg",
    },
]

TIMELINE_CORRECT = [
    "circuito",
    "parque",
    "miraflores",
    "playa",
    "lunahuaná",
    "mandrake",
]
#TIMELINE_CORRECT = TIMELINE.copy()

FINAL_MESSAGE = """
Gracias por jugar este torneo de nuestros recuerdos.

Quise hacerte esto porque cada momento contigo se ha vuelto especial para mí:
desde el Circuito Mágico del Agua, Miraflores, la playa, el anillo de promesa,
nuestras comidas, las manualidades, las flores y, sobre todo, esa canción
tan hermosa que hiciste para mí y que siempre voy a decir que es mi favorita.

Sé que a veces puedo enojarme contigo, pero aun así quiero que nunca olvides esto:
te amo muchísimo, Ismael, y eres una de las partes más bonitas de mi vida.

Por cierto, tal vez no sé mucho de fútbol, pero sí supe hacerte este detalle..
""".strip()

ASSET_VIDEO_PATH = "assets/video_final.mp4"


# =========================================================
# UTILIDADES
# =========================================================
def init_state() -> None:
    defaults = {
        "screen": "home",
        "score": 0,
        "trivia_index": 0,
        "photo_index": 0,
        "completed": [],
        "trivia_feedback": None,
        "photo_feedback": None,
        "crossword_checked": False,
        "crossword_errors": [],
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def mark_completed(key: str, points: int = 0) -> None:
    if key not in st.session_state.completed:
        st.session_state.completed.append(key)
        st.session_state.score += points


def go(screen: str) -> None:
    st.session_state.screen = screen


def reset_game() -> None:
    for key in list(st.session_state.keys()):
        del st.session_state[key]


def local_asset(path_str: str) -> Path | None:
    path = Path(path_str)
    return path if path.exists() else None


def normalize(text: str) -> str:
    replacements = {
        "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U",
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "Ñ": "N", "ñ": "n",
    }
    for a, b in replacements.items():
        text = text.replace(a, b)
    return " ".join(text.upper().split())


def theme_css() -> str:
    c = APP["colores"]
    return f"""
    <style>
    .stApp {{
        background: linear-gradient(180deg, #f8fafc 0%, #ecfeff 100%);
    }}
    @media (prefers-color-scheme: dark) {{
        .stApp {{
            background: linear-gradient(180deg, #0f172a 0%, #0c1a2e 100%) !important;
        }}
    }}
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] h4,
    .stRadio label,
    .stTextInput label,
    .stSelectbox label {{
        color: inherit !important;
    }}
    .hero {{
        padding: 1.6rem 1.2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, {c['azul']} 0%, {c['verde_jade']} 100%);
        color: white !important;
        box-shadow: 0 18px 40px rgba(15,23,42,0.18);
        margin-bottom: 1rem;
    }}
    .hero * {{ color: white !important; }}
    .card {{
        background: white;
        border: 1px solid {c['borde']};
        border-radius: 20px;
        padding: 1rem 1rem;
        box-shadow: 0 8px 20px rgba(15,23,42,0.05);
        margin: 0.6rem 0 1rem 0;
        color: {c['oscuro']} !important;
    }}
    @media (prefers-color-scheme: dark) {{
        .card {{
            background: #1e293b !important;
            border-color: #334155 !important;
            color: #f1f5f9 !important;
        }}
        .card * {{ color: #f1f5f9 !important; }}
        .score {{ color: {c['verde_agua']} !important; }}
    }}
    .badge {{
        display: inline-block;
        padding: 0.28rem 0.70rem;
        border-radius: 999px;
        background: {c['dorado']};
        color: {c['oscuro']} !important;
        font-weight: 700;
        margin: 0.15rem;
    }}
    .center {{ text-align: center; }}
    .score {{
        font-size: 1.1rem;
        font-weight: 700;
        color: {c['azul']};
    }}
    .photo-portrait {{
        max-height: 480px;
        width: auto !important;
        display: block;
        margin: 0 auto;
        border-radius: 12px;
        object-fit: contain;
    }}
    /* Frase revelada */
    .phrase-word {{
        display: inline-block;
        background: {c['azul']};
        color: white !important;
        padding: 0.3rem 0.65rem;
        border-radius: 8px;
        margin: 0.25rem;
        font-weight: 700;
        font-size: 1.1rem;
        letter-spacing: 0.06em;
        user-select: text;
    }}
    .phrase-container {{
        text-align: center;
        padding: 1.2rem 1rem;
        background: #f0f9ff;
        border-radius: 16px;
        border: 2px dashed {c['azul']};
        margin: 1rem 0;
    }}
    @media (prefers-color-scheme: dark) {{
        .phrase-container {{
            background: #1e293b !important;
            border-color: {c['verde_agua']} !important;
        }}
    }}
    </style>
    """


def sidebar() -> None:
    st.sidebar.title("Marcador")
    st.sidebar.markdown(f"**Puntos:** {st.session_state.score}")
    st.sidebar.progress(min(st.session_state.score / 22, 1.0))
    st.sidebar.button("Reiniciar juego", on_click=reset_game, use_container_width=True)


# =========================================================
# HELPER: foto respetando orientación vertical
# =========================================================
def display_photo_or_uploader(photo_cfg: dict, idx: int) -> None:
    path = local_asset(photo_cfg["path"])
    if path:
        import base64, mimetypes
        mime = mimetypes.guess_type(str(path))[0] or "image/jpeg"
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        st.markdown(
            f'<div style="text-align:center">'
            f'<img src="data:{mime};base64,{b64}" class="photo-portrait" />'
            f'</div>',
            unsafe_allow_html=True,
        )
    else:
        st.warning(
            f"No encontré `{photo_cfg['path']}`. Puedes subir la foto aquí "
            f"o ponerla dentro de la carpeta `assets/`."
        )
        upload = st.file_uploader(
            photo_cfg["label"],
            type=["png", "jpg", "jpeg", "webp"],
            key=f"upload_photo_{idx}",
        )
        if upload:
            import base64
            b64 = base64.b64encode(upload.read()).decode()
            mime = upload.type or "image/jpeg"
            st.markdown(
                f'<div style="text-align:center">'
                f'<img src="data:{mime};base64,{b64}" class="photo-portrait" />'
                f'</div>',
                unsafe_allow_html=True,
            )


# =========================================================
# PÁGINAS
# =========================================================
def page_home() -> None:
    st.markdown(
        f"""
        <div class="hero center">
            <h1>{APP['titulo']}</h1>
            <p>{APP['subtitulo']}</p>
            <p>{APP['frase_portada']}</p>
            <p><strong>{APP['firma']}</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    for img_path in OPTIONAL_HERO_IMAGES[:1]:
        path = local_asset(img_path)
        if path:
            st.image(str(path), use_container_width=True)
    st.markdown(
        """
        <div class="card">
        Bienvenido al torneo más importante: el de nuestros recuerdos.
        Aquí vas a pasar por varias rondas para descubrir fotos, apodos,
        momentos especiales y una sorpresa final.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.button("Empezar partido ⚽", on_click=go, args=("rules",), use_container_width=True)


def page_rules() -> None:
    st.header("Cómo se juega")
    st.markdown(
        """
        - **Ronda 1:** Trivia de nosotros.
        - **Ronda 2:** Adivina la foto.
        - **Ronda 3:** Crucigrama — resuelve cada pista para descubrir la frase secreta.
        - **Ronda 4:** ¿Qué pasó primero?
        - **Final:** Premio desbloqueado 🏆
        """
    )
    st.button("Ir a la trivia", on_click=go, args=("trivia",), use_container_width=True)


def page_trivia() -> None:
    idx = st.session_state.trivia_index
    if idx >= len(TRIVIA):
        st.success("¡Terminaste la trivia! ⚽")
        st.button("Siguiente ronda: Adivina la foto", on_click=go, args=("photos",), use_container_width=True)
        return

    q = TRIVIA[idx]
    st.header(f"Ronda 1 — Trivia ({idx + 1}/{len(TRIVIA)})")
    st.markdown(f"<div class='card'><h4>{q['pregunta']}</h4></div>", unsafe_allow_html=True)

    if st.session_state.trivia_feedback is None:
        with st.form(f"trivia_form_{idx}"):
            choice = st.radio("Elige una respuesta", q["opciones"], index=None, key=f"trivia_choice_{idx}")
            submitted = st.form_submit_button("Responder")
        if submitted:
            if choice is None:
                st.warning("Elige una opción antes de responder.")
                return
            chosen_index = q["opciones"].index(choice)
            if chosen_index == q["correcta"]:
                mark_completed(f"trivia_{idx}", 2)
                st.session_state.trivia_feedback = ("success", "¡Golazo! Respuesta correcta.", q["explicacion"])
            else:
                st.session_state.trivia_feedback = ("error", "Casi... esa no era.", q["explicacion"])
            st.rerun()
    else:
        kind, title, explanation = st.session_state.trivia_feedback
        if kind == "success":
            st.success(title)
        else:
            st.error(title)
        st.caption(explanation)
        if st.button("Siguiente pregunta", key=f"next_trivia_{idx}", use_container_width=True):
            st.session_state.trivia_index += 1
            st.session_state.trivia_feedback = None
            st.rerun()


def page_photos() -> None:
    idx = st.session_state.photo_index
    if idx >= len(PHOTO_ROUNDS):
        st.success("¡Terminaste la ronda de fotos!")
        st.button("Siguiente ronda: Crucigrama", on_click=go, args=("crossword",), use_container_width=True)
        return

    item = PHOTO_ROUNDS[idx]
    st.header(f"Ronda 2 — Adivina la foto ({idx + 1}/{len(PHOTO_ROUNDS)})")

    if st.session_state.photo_feedback is None:
        display_photo_or_uploader(item, idx)
        st.markdown(f"**{item['pregunta']}**")
        with st.form(f"photo_form_{idx}"):
            choice = st.radio("Tu respuesta", item["opciones"], index=None, key=f"photo_choice_{idx}")
            submitted = st.form_submit_button("Comprobar")
        if submitted:
            if choice is None:
                st.warning("Elige una opción antes de continuar.")
                return
            chosen_index = item["opciones"].index(choice)
            if chosen_index == item["correcta"]:
                mark_completed(f"photo_{idx}", 2)
                st.session_state.photo_feedback = ("success", "¡Sí fue ese momento!", item["explicacion"])
            else:
                st.session_state.photo_feedback = ("error", "Uy, no era ese recuerdo.", item["explicacion"])
            st.rerun()
    else:
        display_photo_or_uploader(item, idx)
        kind, title, explanation = st.session_state.photo_feedback
        if kind == "success":
            st.success(title)
        else:
            st.error(title)
        st.caption(explanation)
        if st.button("Siguiente foto", key=f"next_photo_{idx}", use_container_width=True):
            st.session_state.photo_index += 1
            st.session_state.photo_feedback = None
            st.rerun()


def page_crossword() -> None:
    st.header("Ronda 3 — Crucigrama secreto 🔐")
    st.markdown(
        "Resuelve cada pista. Cuando completes **todas correctamente**, "
        "las palabras formarán una frase especial."
    )

    already_solved = "crossword" in st.session_state.completed
    errors: list[int] = st.session_state.get("crossword_errors", [])
    answers: list[str] = []

    for clue in CROSSWORD:
        n = clue["num"]
        length = len(clue["respuesta"])
        blanks = "_ " * length

        st.markdown(f"**{n}.** {clue['pista']}  \n`{blanks.strip()}`")
        val = st.text_input(
            f"Respuesta {n}",
            key=f"cross_{n}",
            label_visibility="collapsed",
            disabled=already_solved,
            max_chars=length + 2,
        )
        answers.append(val)

        if n in errors:
            st.caption(f"⚠️ Revisa la respuesta {n}.")

        st.markdown("---")

    if not already_solved:
        if st.button("Revisar crucigrama 🔍", use_container_width=True):
            new_errors = [
                clue["num"]
                for i, clue in enumerate(CROSSWORD)
                if normalize(answers[i]) != normalize(clue["respuesta"])
            ]
            st.session_state.crossword_errors = new_errors
            st.session_state.crossword_checked = True

            if not new_errors:
                mark_completed("crossword", 4)
            st.rerun()

        if st.session_state.crossword_checked and errors:
            st.warning(
                f"Hay {len(errors)} respuesta(s) por corregir (marcadas con ⚠️ arriba). ¡Sigue intentando!"
            )

    # Frase revelada cuando está resuelto
    if already_solved:
        st.success("¡Crucigrama resuelto! Aquí está la frase que formaste:")
        words_html = " ".join(
            f'<span class="phrase-word">{c["respuesta"]}</span>'
            for c in CROSSWORD
        )
        st.markdown(
            f'<div class="phrase-container">{words_html}</div>',
            unsafe_allow_html=True,
        )
        st.caption("💙 De tu cachetona")
        st.button("Ir a ¿Qué pasó primero?", on_click=go, args=("timeline",), use_container_width=True)


def page_timeline_antiguo() -> None:
    st.header("Ronda 4 — ¿Qué pasó primero?")
    st.markdown("Ordena estos recuerdos del primero al último.")

    selected = []
    options = ["-- Elegir --"] + TIMELINE
    for i in range(len(TIMELINE)):
        selected.append(st.selectbox(f"Posición {i + 1}", options, key=f"timeline_{i}"))

    if st.button("Revisar orden", use_container_width=True):
        chosen = [s for s in selected if s != "-- Elegir --"]
        if len(chosen) != len(TIMELINE):
            st.warning("Completa todas las posiciones.")
            return
        if len(set(chosen)) != len(TIMELINE):
            st.warning("Cada recuerdo debe usarse una sola vez.")
            return
        if selected == TIMELINE_CORRECT:
            mark_completed("timeline", 4)
            st.success("¡Perfecto! Sí recuerdas la secuencia de nuestra historia.")
        else:
            st.error("Casi... el orden no era ese. Puedes volver a intentarlo.")

    if "timeline" in st.session_state.completed:
        st.button("Desbloquear premio final 🏆", on_click=go, args=("final",), use_container_width=True)

def page_timeline() -> None:
    st.header("Ronda 4 — ¿Qué pasó primero?")
    st.markdown("Ponle un número a cada foto según el orden correcto.")

    positions = ["-- Elegir --"] + list(range(1, len(TIMELINE_ITEMS) + 1))
    selected_positions = []

    cols = st.columns(2)

    for i, item in enumerate(TIMELINE_ITEMS):
        with cols[i % 2]:
            st.markdown(f"**{item['label']}**")
            display_photo_or_uploader(item, f"timeline_{i}")

            pos = st.selectbox(
                "Posición",
                positions,
                key=f"timeline_pos_{item['id']}",
            )

            selected_positions.append((item["id"], pos))

    if st.button("Revisar orden", use_container_width=True):
        chosen = [pos for _, pos in selected_positions]

        if "-- Elegir --" in chosen:
            st.warning("Asigna una posición a cada foto.")
            return

        if len(set(chosen)) != len(TIMELINE_ITEMS):
            st.warning("Cada posición debe usarse una sola vez.")
            return

        ordered_ids = [
            item_id
            for item_id, pos in sorted(selected_positions, key=lambda x: x[1])
        ]

        if ordered_ids == TIMELINE_CORRECT:
            mark_completed("timeline", 4)
            st.success("¡Perfecto! Sí recuerdas la secuencia de nuestra historia.")
        else:
            st.error("Casi... el orden no era ese. Puedes volver a intentarlo.")

    if "timeline" in st.session_state.completed:
        st.button(
            "Desbloquear premio final 🏆",
            on_click=go,
            args=("final",),
            use_container_width=True,
        )
        
def page_final() -> None:
    st.header("Premio desbloqueado 🏆")
    st.markdown(
        f"""
        <div class="card">
            <p class="score">Puntaje final: {st.session_state.score}</p>
            <p>{FINAL_MESSAGE.replace(chr(10), "<br>")}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    video_path = local_asset(ASSET_VIDEO_PATH)
    if video_path:
        st.video(str(video_path))
    else:
        st.info("Pon tu video como `assets/video_final.mp4` o súbelo aquí.")
        upload = st.file_uploader("Sube el video final", type=["mp4", "mov", "m4v"], key="final_video")
        if upload:
            st.video(upload)

    st.markdown("### Mensaje final")
    st.write(
        f"{APP['nombre']}, gracias por ser parte de esta historia tan bonita. "
        f"{APP['frase_final']}"
    )

    c1, c2 = st.columns(2)
    with c1:
        st.button("Volver al inicio", on_click=go, args=("home",), use_container_width=True)
    with c2:
        st.button("Jugar otra vez", on_click=reset_game, use_container_width=True)


# =========================================================
# APP
# =========================================================
def main() -> None:
    st.set_page_config(
        page_title=APP["titulo"],
        page_icon="⚽",
        layout="centered",
    )
    init_state()
    st.markdown(theme_css(), unsafe_allow_html=True)
    sidebar()

    screens = {
        "home":      page_home,
        "rules":     page_rules,
        "trivia":    page_trivia,
        "photos":    page_photos,
        "crossword": page_crossword,
        "timeline":  page_timeline,
        "final":     page_final,
    }
    screens.get(st.session_state.screen, page_home)()


if __name__ == "__main__":
    main()

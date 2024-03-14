import streamlit as st
from googletrans import Translator, LANGUAGES


def main():
    st.title("Tradutor de Idiomas")
    translator = Translator()

    # Entrada do texto
    texto = st.text_area("Insira o texto a ser traduzido", "")

    # Detecção automática de idioma
    idioma_origem = translator.detect(texto).lang if texto else "Auto"

    # Seleção do idioma de destino
    idioma_destino = st.selectbox(
        "Selecione o idioma de destino", [LANGUAGES[lang] for lang in LANGUAGES]
    )

    if st.button("Traduzir"):
        if texto:
            try:
                resultado = translator.translate(
                    texto,
                    src=idioma_origem,
                    dest=list(LANGUAGES.keys())[
                        list(LANGUAGES.values()).index(idioma_destino)
                    ],
                )
                st.success(resultado.text)
            except ValueError as e:
                st.error(str(e))
        else:
            st.warning("Por favor, insira um texto para traduzir.")


if __name__ == "__main__":
    main()

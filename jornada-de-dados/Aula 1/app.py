import streamlit as st

def hello_world() -> str:
    return "Olá, essa é minha aplicação"

def main():
    st.write(hello_world())

if __name__ == "__main__":
    main()
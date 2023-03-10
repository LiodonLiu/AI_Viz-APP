import streamlit as st
from location import locate
from PIL import Image

def main():
    menu = ["首页","登录", "退出"]

    if 'count' not in st.session_state:
        st.session_state.count = 0

    choice = st.sidebar.selectbox("选项",menu)
    st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 250px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 250px;
        margin-left: -250px;
    }
    </style>
    """,
    unsafe_allow_html=True,)

    if choice =="首页":
        st.subheader("首页")
        st.markdown('''Streamlit文档的地址是：https://docs.streamlit.io/''')
        st.title("欢迎使用自动化语言图像生成")

    elif choice =="登录":
        st.sidebar.subheader("登录区域")

        username = st.sidebar.text_input("用户名")
        if st.sidebar.checkbox("开始登录"):
          st.sidebar.success("您已登录成功，您的用户名是 {}".format(username))
          st.title("AI-VIZ")
        #   st.balloons()
          form1 = st.form(key='my_form1')
          input_text = form1.text_input('input text:', 'An ice cream near the door')
          submit_button = form1.form_submit_button(label = 'Submit')
          if submit_button:
            locate(input_text)
            image = Image.open('final_canvas.jpg')
            st.image(image, caption='final_canvas') 
        else:
          st.title("请先登录")

    elif choice =="退出":
        st.session_state.count = 0
        if st.session_state.count == 0:
            st.info("您已成功退出，如果需要，请选择左侧的登录按钮继续登录。")



if __name__=="__main__":
    main()

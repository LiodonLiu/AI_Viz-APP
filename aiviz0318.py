import streamlit as st
from location import locate
from PIL import Image

def main():
    st.markdown('''<a href="http://www.baidu.com">
        <button>
        <font face="幼圆" size=2>问题反馈</font>
        </button>
    </a>''',unsafe_allow_html=True)
    st.markdown('''<a href="https://note.youdao.com/s/NGGNVkbn">
        <button>
        <font face="幼圆" size=2>隐私政策</font>
        </button>
    </a>''',unsafe_allow_html=True)
    placeholder = st.empty()
    if placeholder.checkbox("开始使用"):
          placeholder.empty()
          st.title("AI-VIZ")
          form1 = st.form(key='my_form1')
          input_text = form1.text_input('输入：', 'An ice cream near the door')
          submit_button = form1.form_submit_button(label = '提交')
          if submit_button:
            locate(input_text)
            image = Image.open('final_canvas.jpg')
            st.image(image, caption='final_canvas') 
            with open("final_canvas.jpg", "rb") as file:
                btn = st.download_button(
                        label="下载",
                        data=file,
                        file_name=input_text + '.jpg',
                        mime="image/jpg"
                      )
    else:
        st.markdown('''<font face="幼圆" size=7><b>使用详情见下</b></font>''', unsafe_allow_html=True)
        st.markdown('''<div style="text-indent:2em;"><font face="幼圆" size=3>①在“输入”框中输入<u>英文</u>语句</font></div>''', unsafe_allow_html=True)
        st.markdown('''<div style="text-indent:2em;"><font face="幼圆" size=3>②点击下方“提交”按钮</font></div>''', unsafe_allow_html=True)
        st.markdown('''<div style="text-indent:2em;"><font face="幼圆" size=3>③静待图片生成</font></div>''', unsafe_allow_html=True)
        st.markdown('''<div style="text-indent:2em;"><font face="幼圆" size=3>④图片生成后，可点击“下载”按钮下载图片</font></div>''', unsafe_allow_html=True)
        st.markdown('''<div style="text-indent:2em;"><font face="幼圆" size=3>⑤使用过程中有任何问题，欢迎点击上方“问题反馈”按钮与我们联系！</font></div>''', unsafe_allow_html=True)
    st.markdown('''<style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div:nth-child(1) > div > div > a > button{
      position:absolute;left:80%;top:-50px;
      border-color: white;background-color: white;border-style: unset
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div:nth-child(2) > div > div > a > button{
      position:absolute;left:80%;top:-30px;border-color: #4478C3;background-color: white;border-radius: 10px
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div:nth-child(3) > div > label > div > div > div > p{
      font-family: YouYuan;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div.css-12ttj6m.epcbefy1 > div:nth-child(1) > div > div:nth-child(1) > div > label > div > p{
      font-family: YouYuan;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div.css-12ttj6m.epcbefy1 > div:nth-child(1) > div > div:nth-child(2) > div > div > button > div > p{
      font-family: YouYuan;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div.css-12ttj6m.epcbefy1{
      border: 1px solid #4478C3;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div.css-12ttj6m.epcbefy1 > div:nth-child(1) > div > div:nth-child(2) > div > div > button{
      border: 1px solid #4478C3;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div:nth-child(7) > div > button{
      border: 1px solid #4478C3;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-91z34k.egzxvld4 > div:nth-child(1) > div > div:nth-child(7) > div > button > div > p{
      font-family: YouYuan;
      }
      </style>''', unsafe_allow_html=True)

if __name__=="__main__":
    main()

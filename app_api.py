import streamlit as st
from location import locate
from PIL import Image

def main():
    st.markdown('''<a href="https://docs.qq.com/form/page/DRXdqRnl4THpWVXFM#/fill">
        <button>
        <font face="幼圆" size=2>问题反馈</font>
        </button>
    </a>''',unsafe_allow_html=True)
    st.markdown('''<font face="幼圆" size=2>问题反馈</font></a>''',unsafe_allow_html=True)
    placeholder = st.empty()
    if placeholder.checkbox("同意"):
          placeholder.empty()
          st.title("AI-VIZ")
          tab1, tab2= st.tabs(["稳定模式", "自由模式"])
          with tab1:
            st.header("稳定模式")
            option1 = st.selectbox('请选择名词A',('ice cream', 'table', 'tree', 'door', 'house', 'cat', 'tea'))
            option2 = st.selectbox('请选择名词B',('ice cream', 'table', 'tree', 'door', 'house', 'cat', 'tea'))
            option3 = st.selectbox('请选择二者介词关系',('beneath','before','around','behind','inside','near','on','under','among'))
            option = option1 + ' ' + option3 + ' ' + option2
            st.write('输入语句为：'+ option)
            choose_button = st.button(label = '确认')
            if choose_button:
              try:
                locate(option)
                image = Image.open('final_canvas.jpg')
                st.image(image, caption='final_canvas') 
                with open("final_canvas.jpg", "rb") as file:
                    btn = st.download_button(
                            label="下载",
                            data=file,
                            file_name=option + '.jpg',
                            mime="image/jpg"
                          )
              except:
                st.error('运行出错', icon="🚨")
          with tab2:
            st.header("自由模式")
            form1 = st.form(key='my_form1')
            input_text = form1.text_input('输入：')
            submit_button = form1.form_submit_button(label = '提交')
            if submit_button:
              try:
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
              except:
                st.error('运行出错', icon="🚨")
    else:
        st.markdown('''<font face="幼圆" size=7><b>使用详情见下</b></font>''', unsafe_allow_html=True)
        st.markdown('''<div style="text-indent:2em;"><font face="幼圆" size=3>①在“输入”框中输入<b>英文</b>语句</font></div>''', unsafe_allow_html=True)
        st.markdown('''<div style="text-indent:2em;"><font face="幼圆" size=3>②点击下方“提交”按钮</font></div>''', unsafe_allow_html=True)
        st.markdown('''<div style="text-indent:2em;"><font face="幼圆" size=3>③静待图片生成</font></div>''', unsafe_allow_html=True)
        st.markdown('''<div style="text-indent:2em;"><font face="幼圆" size=3>④图片生成后，可点击“下载”按钮下载图片</font></div>''', unsafe_allow_html=True)
        st.markdown('''<div style="text-indent:2em;"><font face="幼圆" size=3>⑤使用过程中有任何问题，欢迎点击上方“问题反馈”按钮与我们联系！</font></div>''', unsafe_allow_html=True)
        st.markdown('''<a href="https://note.youdao.com/s/NGGNVkbn">
            <button>
            <font face="幼圆"><u>隐私政策</u></font>
            </button>
            </a>''',unsafe_allow_html=True)
        st.markdown('''<font face="幼圆"><u>隐私政策</u></font></a>''',unsafe_allow_html=True)
    st.markdown('''<style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.egzxvld4 > div:nth-child(1) > div > div:nth-child(1) > div > div > a > button{
      border-color: rgba(0,0,0,0);background-color: rgba(0,0,0,0);position: fixed;top: 50px;right: 0px;z-index:1;color: rgba(0,0,0,0);
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.egzxvld4 > div:nth-child(1) > div > div:nth-child(2) > div > div > p > font{
      position: fixed;top: 56px;right: 7px;z-index:0;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.egzxvld4 > div:nth-child(1) > div > div:nth-child(10) > div > div > a > button{
      border-color: rgba(0,0,0,0);background-color: rgba(0,0,0,0);position: fixed;bottom: 5px;left: 73px;z-index:1;color: rgba(0,0,0,0);
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.egzxvld4 > div:nth-child(1) > div > div:nth-child(11) > div > div > p > font > u{
      position: fixed;bottom: 8px;left: 80px;z-index:0;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > footer{
      color: rgba(0,0,0,0);background: rgba(0,0,0,0);
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > footer > a{
      cursor: not-allowed;pointer-events: none;color: rgba(0,0,0,0);
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.egzxvld4 > div:nth-child(1) > div > div:nth-child(3) > div > label{
      position: fixed;bottom: 9px;left: 20px;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.egzxvld4 > div:nth-child(1) > div > div:nth-child(3) > div > label > div > div > div > p{
      font-family: YouYuan;
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > header > div.css-14xtw13.e8zbici0{
      color: rgba(0,0,0,0);
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > header > div.css-14xtw13.e8zbici0 > div:nth-child(1) > button{
      cursor: not-allowed;pointer-events: none;color: rgba(0,0,0,0);
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > header > div.css-14xtw13.e8zbici0 > div:nth-child(2) > button{
      cursor: not-allowed;pointer-events: none;color: rgba(0,0,0,0);
      }
    #root > div:nth-child(1) > div.withScreencast > div > div > header > div.css-14xtw13.e8zbici0 > div:nth-child(3) > button{
      cursor: not-allowed;pointer-events: none;color: rgba(0,0,0,0);
      }
    #MainMenu > button{
      cursor: not-allowed;pointer-events: none;color: rgba(0,0,0,0);
      }
    </style>''', unsafe_allow_html=True)

if __name__=="__main__":
    main()

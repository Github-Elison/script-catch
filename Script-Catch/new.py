import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from colorthief import ColorThief
from fontTools.ttLib import TTFont
import io


def get_styles(url):
    driver = None
    try:
        # Configuração do driver do Selenium
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=options)

        # Carrega a página usando o Selenium para lidar com carregamento dinâmico
        driver.get(url)

        # Extrai os estilos CSS embutidos na página
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        styles = soup.find_all('style')
        for style in styles:
            print(style.get_text())

        # Extrai os estilos de arquivos de estilo externos
        external_styles = soup.find_all('link', rel='stylesheet')
        for external_style in external_styles:
            external_style_url = external_style.get('href')
            if external_style_url:
                external_style_content = requests.get(external_style_url).text
                print(external_style_content)

        # Tira uma captura de tela para processamento de imagem
        screenshot = driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(screenshot))

        # Analisa cores da imagem usando a biblioteca ColorThief
        color_thief = ColorThief(image)
        dominant_color = color_thief.get_color(quality=1)
        palette = color_thief.get_palette(color_count=6)

        print(f"Dominant Color: {dominant_color}")
        print(f"Color Palette: {palette}")

        # Analisa as fontes utilizadas na página
        font_urls = set()
        for font_face in soup.find_all('style', {'type': 'text/css'}):
            font_urls.update([url.strip("('')")
                             for url in font_face.get_text().split('url(') if url])

        for font_url in font_urls:
            font_data = requests.get(font_url).content
            font = TTFont(io.BytesIO(font_data))
            font_properties = font['name'].getName(4, 3, 1)
            print(f"Font Family: {font_properties.string.decode('utf-16')}")
            print(f"Font URL: {font_url}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        if driver:
            driver.quit()


def main():
    url = input("https://www.unibf.com.br/")
    get_styles(url)


if __name__ == "__main__":
    main()

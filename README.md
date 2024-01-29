# Web Scraping e Análise de Estilos - Script Python

Este script em Python foi desenvolvido para realizar web scraping em um site fornecido pelo usuário, extraindo informações sobre estilos CSS, cores da imagem e fontes de texto utilizadas.

## Funcionalidades

O script realiza as seguintes operações:

1. **Web Scraping de Estilos CSS:**
   - Extrai estilos CSS embutidos na página.
   - Extrai estilos de arquivos de estilo externos vinculados à página.

2. **Análise de Cores da Imagem:**
   - Captura uma tela do site e analisa a cor dominante.
   - Gera uma paleta de cores da imagem.

3. **Identificação de Fontes de Texto:**
   - Analisa os estilos CSS para identificar URLs de fontes.
   - Baixa as fontes e extrai informações sobre a família da fonte.

## Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)

## Instalação de Dependências

Instale as bibliotecas necessárias utilizando o seguinte comando:

```bash
pip install requests beautifulsoup4 selenium Pillow colorthief fonttools webdriver_manager
Execução
Abra um terminal ou prompt de comando.
Navegue até o diretório onde o script está localizado.
Execute o script com o comando:
bash
Copy code
python caminho/para/seu/script.py
Substitua "caminho/para/seu/script.py" pelo caminho real para o seu script Python.

Notas Adicionais
Certifique-se de ter o ChromeDriver instalado ou configurado corretamente para o Selenium.
Este script foi projetado para fins educacionais e pode necessitar de ajustes para diferentes casos de uso.
csharp
Copy code

Este README fornece uma visão geral do propósito do script, instruções de instalação e execução, bem como notas adicionais para informações específicas sobre o ambiente de execução. Lembre-se de adaptar as instruções conforme necessário para atender às necessidades do seu projeto.

# Scrapy_Fundos_Imobiliarios_Filtrados
<h3> Crawler que capta e filtra Fundos Imobiliários ultilizando o site fundamentus.com.br</h3>

![Captura de tela 2021-09-03 181318](https://user-images.githubusercontent.com/53584953/132065825-ab14935f-328f-4c9b-98d3-ddd2d3cc4858.png)

### Video de onde codigo foi inspirado.
[![IMAGE ALT TEXT HERE](https://i.ytimg.com/vi/IazEN13o304/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCc3Ks7-FTNBaeHO91dnjDhCETYFw)](https://www.youtube.com/watch?v=IazEN13o304&t=984s&ab_channel=OPrimoRico)

Video produzido pelo canal Primo Rico.



<strong>Itens ultilizados e versoniamentos:</strong>
* Python 3.9.0
* Scrapy 2.4.1 

<strong>Preciso baixar algo?</strong><br>
É necessario ter o Python instalado e o Scrapy (*pip install scrapy*); Por ultimo, ter uma IDE de sua preferencia, para rodar o projeto.<br>

<strong>Como faço para funcionar o codigo?</strong>
* Basta baixar ou clonar o codigo, caso não tenha instalado o <strong>Scrapy</strong>, instale ele (*pip install scrapy*).
* Abra o terminal e esteja dentro da pasta do projeto, depois basta rodar o comando: <br>
 **scrapy crawl procuraFII -o** *(nome do arquivo a ser gerado + .csv ou qualquer extensão desejada)*.<br>
 **Exemplo**: scrapy crawl procuraFII -o DadosFundosImobiliarios.csv
 
 ![terminal mostrando o codigo para rodar o projeto](https://user-images.githubusercontent.com/53584953/131869633-c23adc4e-c762-4ea3-b1fa-2a629e50aedc.png)


### Onde vejo o codigo que foi criado e posso alteralo?
#### Caso deseja alterar a esturua do codigou ou A estrutura do site seja alterada e o Xpaht não funione mais.

* Entre na pasta *Spiders*, abra o arquivo **procuraFII** e lá será encontrado todos o codigo feito e seu comentario explicando cada função. 

![mostrando onde fica o procuraFII](https://user-images.githubusercontent.com/53584953/131869698-8579ad00-1794-4137-bdaa-467059e409b0.png)

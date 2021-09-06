# Scrapy_Fundos_Imobiliarios_Filtrados
<h3> Crawler que capta e filtra Fundos Imobiliários ultilizando o site fundamentus.com.br</h3>

![Captura de tela 2021-09-03 181318](https://user-images.githubusercontent.com/53584953/132065825-ab14935f-328f-4c9b-98d3-ddd2d3cc4858.png)

### Vídeo explicando como o codigo foi feito. 
[![IMAGE ALT TEXT HERE](https://i9.ytimg.com/vi/dK7pLhqVl-Y/mqdefault.jpg?v=61366866&sqp=CIjP2YkG&rs=AOn4CLBYXH7tZWLLw9fERLy7KiyDM0_Dvg)](https://youtu.be/dK7pLhqVl-Y)
<br>*(Clique na imamge para ser redirecionado)*


### Vídeo de onde codigo foi inspirado.
[![IMAGE ALT TEXT HERE](https://i.ytimg.com/vi/IazEN13o304/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCc3Ks7-FTNBaeHO91dnjDhCETYFw)](https://www.youtube.com/watch?v=IazEN13o304&t=984s&ab_channel=OPrimoRico)
<br>*(Clique na imamge para ser redirecionado)*

***
### Objetivo do codigo:
* Coletar todos os dados dos Fundos Imobiliários.
* Filtra os dados por meio do filtro apresentado no video do Primo Rico.

**Qual o filtro apresentado no video?**
>**Dividendo Yield:** Maior que 4%   
>**P / PV:** Maior que 0.4 e menor que 1.2 <br>
>**Valor de mercado:** Maior que 500M (500.000.000) <br>
>**Vacancia:** Menor que 30%<br>
>**Liquidez:** Mais que 1M (1.000.000)

**Link para a versão do código que coleta todos os dados sem filtro:** <br>
https://github.com/andreboa-sorte/Scrapy_Fundos_Imobiliarios

***

<strong>Itens ultilizados e versoniamentos:</strong>
* Python 3.9.0
* Scrapy 2.4.1 

<strong>Preciso baixar algo?</strong><br>
É necessario ter o Python instalado e o Scrapy (*pip install scrapy*); Por ultimo, ter uma IDE de sua preferencia, para rodar o projeto.<br>

<strong>Como faço para funcionar o codigo?</strong>
* Basta baixar ou clonar o codigo, caso não tenha instalado o <strong>Scrapy</strong>, instale ele (*pip install scrapy*).
* Abra o terminal e esteja dentro da pasta do projeto, depois basta rodar o comando: <br>
 **scrapy crawl FIIComFiltro -o** *(nome do arquivo a ser gerado + .csv ou qualquer extensão desejada)*.<br>
 **Exemplo**: scrapy crawl FIIComFiltro -o DadosFIIsFiltrados.csv
 
![teminal](https://user-images.githubusercontent.com/53584953/132256807-e0cb4b61-924b-426f-9438-4a72b1720368.png)



### Onde vejo o codigo que foi criado e posso alteralo?
#### Caso deseja alterar a esturua do codigou ou A estrutura do site seja alterada e o Xpaht não funione mais.

* Entre na pasta *Spiders*, abra o arquivo **FIIComFiltro** e lá será encontrado todos o codigo feito e seu comentario explicando cada função. 

![fiicomfiltro](https://user-images.githubusercontent.com/53584953/132256870-058f8b0a-715b-4391-affa-c0a79f95bc41.png)


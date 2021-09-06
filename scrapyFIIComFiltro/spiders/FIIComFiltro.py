import scrapy


class FiicomfiltroSpider(scrapy.Spider):
    name = 'FIIComFiltro'
    #allowed_domains = ['www.fundamentus.com.br/fii_resultado.php']
    start_urls = ['http://www.fundamentus.com.br/fii_resultado.php/']  # o link q sera "scrapydo".
                                                                        # como é somente vamos pegar os dados de um demonio,
                                                                        # então não vamos usar o allowed_domains

    def parse(self, response):
        lista = response.xpath('//*[@id="tabelaResultado"]/tbody/tr')
        i = 0
        for itemlita in lista:  # um laço de repetição para pegar todos os dados da "caixa grande"
            i = int(i) #como é um laço de repetição, o i que abaixo se trasnformou em STR, tem q voltar a ser int, para poder ser incrementado
            i = i + 1
            i = str(i) #transforma o i em str para poder ser adicionado a string do Xpath
            # aqui nesse parte onde é pego os dados que se deseja exrair e é botado nas variaveis
            Papel = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[1]/span/a/text()').extract_first()
            Segmento = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[2]/text()').extract_first()
            Cotacao = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[3]/text()').extract_first()
            FFOYield = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[4]/text()').extract_first()
            DividendYield = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[5]/text()').extract_first()
            P_VP = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[6]/text()').extract_first()
            ValorMercado = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[7]/text()').extract_first()
            Liquidez = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[8]/text()').extract_first()
            QtdImoveis = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[9]/text()').extract_first()
            PrecoP_M2 = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[10]/text()').extract_first()
            AlugelP_M2 = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[11]/text()').extract_first()
            CapRate = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[12]/text()').extract_first()
            VacanciaMed = itemlita.xpath('//*[@id="tabelaResultado"]/tbody/tr[' + i + ']/td[13]/text()').extract_first()

            '''filtro a ser criado
            dividendo yield : maior que 4% 
            p / pv: maior que 0.4 e menor que 1.2
            valor de mercado: maior que 500M (500.000.000) 
            vacancia: menor que 30% (0.3)
            liquidez: mais que 1M (1.000.000)
            '''
            #Aqui é onde estamos preparando e convetando os dados brutos em dados que possam ser lidos pelo nosso if
            DividendYield = DividendYield.strip('%')
            DividendYield = DividendYield.replace("," , ".")
            DividendYield = float(DividendYield)

            P_VP = P_VP.replace(",", ".")
            P_VP = float(P_VP)

            ValorMercado = ValorMercado.replace("." , "")
            ValorMercado = int(ValorMercado)

            VacanciaMed = VacanciaMed.strip('%')
            VacanciaMed = VacanciaMed.replace(",", ".")
            VacanciaMed = float(VacanciaMed)

            Liquidez = Liquidez.replace("." , "")
            Liquidez = int(Liquidez)

            #if com as condições apresentada na filtro acima
            condicao = ((DividendYield > 4.00) and (P_VP > 0.40) and (P_VP < 1.20) and (ValorMercado > 5000000000) and
                        (VacanciaMed < 30.00) and (Liquidez > 1000000))
            if condicao:
                #aqui estamos adicionando novamente a % para os dados, para que possa ser salvas de maneira mais legivel
                DividendYield = str(DividendYield)
                DividendYield = (DividendYield + "%")
                VacanciaMed = str(VacanciaMed)
                VacanciaMed = (VacanciaMed + "%")
                # o "yield" é o comando ultilizado para ele fazer uma função ou interação
                yield {  # depois de coletados, as informações são organizadas para q possão ser salvas e são salvas depois
                    'Papel': Papel,
                    'Segmento': Segmento,
                    'Cotacao': Cotacao,
                    'FFOYield': FFOYield,
                    'DividendYield': DividendYield,
                    'P/VP': P_VP,
                    'ValorMercado': ValorMercado,
                    'Liquidez': Liquidez,
                    'QuantidadeDeImoveis': QtdImoveis,
                    'PrecoPorM2': PrecoP_M2,
                    'AlugelPorM2': AlugelP_M2,
                    'CapRate': CapRate,
                    'VacanciaMedia': VacanciaMed,
                }

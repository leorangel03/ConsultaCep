# ConsultarCEP
Abrange consultas de endereços em cima de um arquivo '.xlsx' para buscar os ceps respectivos através de API's.

#### Foram utilizadas duas API's para realizar as consultas, ViaCep(https://viacep.com.br/) e OpenCageData(https://opencagedata.com/)

* ViaCep serviu para buscar os ceps pelo estado, municipio e rua, segue a url:
  ![image](https://github.com/leorangel03/ConsultarCEP/assets/110949069/00785750-acff-4b48-9b34-7a6decb6452c)

* OpenCageData utilizado para consultar os ceps através da longitude e latitude, segue a url:
![image](https://github.com/leorangel03/ConsultarCEP/assets/110949069/c50791a8-cb99-42a7-8790-174f556e9894)
  * Ressaltando que para utilizar o OpenCageData é ncessario uma Api_Key adquirida pelo site da API
 
#### No repósitorio sera disponibilizado os arquivos '.xlsx' e '.py' onde contem os seguites usos:
* Lib Pandas - para manipulação de arquivos xlsx e dataframes
* Lib Requests - para requisição das API's
* Lógicas para manipulação de strings
* Estrutura para manipular listas
* Funçoes para realizar as requisiçoes e obter somente o 'CEP'

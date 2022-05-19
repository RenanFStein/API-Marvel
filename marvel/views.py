from ast import Raise
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import hashlib
import requests as rq
import time
from django.contrib import messages

# Create your views here.
@login_required(login_url='index')
def home(request):
     

        if request.method == 'POST':
            pesquisa = {}
            try:
                print(str(request.POST['search']))

                publicKey = '7e7f54fed420a83880c1e46f8e66cc62'
                privateKey = 'e92d37bb7c7dcaaa9d17dd693b7b41c44891f3ea'
                
                m= hashlib.md5() # Chama a Função para criptografia
                ts = str(time.time()) # coleta o tempo atual

                m.update(bytes(ts,'utf-8')) 
                m.update(bytes(privateKey, 'utf-8'))
                m.update(bytes(publicKey, 'utf-8'))
                hasht = m.hexdigest() # Cria o MD5
                
                # Montando a URL
                base = 'https://gateway.marvel.com' # Pag base para todas as requests
                personagem = str(request.POST['search'])
                requisicao = (f"/v1/public/characters?name={personagem}&orderBy=name&limit=1")

                url = (f'{base}{requisicao}&ts={ts}&apikey={publicKey}&hash={hasht}' )      
                dados = rq.get(url).json()  
                print(dados)
            
                descricao = dados['data']['results']
                imgpath = dados['data']['results'][0]['thumbnail']['path']
                imgext = dados['data']['results'][0]['thumbnail']['extension']
                print('Sucesso')
                print(descricao)
                print('****')
                pesquisa={
                            'nome' : (dados['data']['results'][0]['name']),
                            'imagem': (f'{imgpath}.{imgext}'),
                            'description' : (dados['data']['results'][0]['description'])
                            }
                
                
                return render(request, 'home.html', pesquisa)
            
            except IndexError:              
                messages.warning(request,'Personagem indisponivel no momento')
                return render(request, 'home.html', pesquisa)
            except KeyError:           
            
                messages.error(request, 'Campo não pode ficar vazio')
                return render(request, 'home.html', pesquisa)
            except ValueError:
                print('Erro1')
                return render(request, 'home.html', pesquisa)
        return render(request, 'home.html')

    

    
from flask import Flask, render_template_string
import random
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz
 
# Lista de alunos
total_alunos = [
    "Ana Bia", "Beatriz", "Bianca", "Cachoeira", "Eduardo memes", "Eduardo",
    "Tabuchi", "Geovanna", "Juan", "Lucas", "Matheus", "Pedro henrique",
    "Pedro moises", "Renato", "Samira", "Will", "Piassi", "Heitor",
    "Joao vitor", "Maria eduarda", "Mayla", "Camilla", "Nicolas", "Enrico"
]
 
app = Flask(__name__)
mesas = []
 
# Função para distribuir os alunos nas mesas
def distribuir_alunos():
    global mesas
    alunos = total_alunos.copy()
    random.shuffle(alunos)
    mesas = [[] for _ in range(5)]
   
    for i in range(4):
        for mesa in mesas:
            mesa.append(alunos.pop())
 
    while alunos:
        for mesa in mesas:
            if alunos:
                mesa.append(alunos.pop())
 
def schedule_task():
    timezone = pytz.timezone('America/Sao_Paulo')
    scheduler = BackgroundScheduler()
    scheduler.add_job(distribuir_alunos, 'cron', hour=6, minute=0, timezone=timezone)
    scheduler.start()
 
# Rota principal que exibe as mesas
@app.route('/')
def show_mesas():
    html_template = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Rodizio de mesa</h1>
    <div class="grid">
        <div style="color: #9eb7cf;" class="professor">
            <h3>Mesa do professor</h3>
        </div>

        <div class="corredor ">
            <h3 class="vertical-text" style="color: #9eb7cf;">Corredor</h3>
        </div>
        <div class="lousa">
            <h3>Lousa</h3>
        </div>
        <div class="mesa2">
            <div class="circulo">
                <h2>Mesa 2</h2>
            </div>
            <div class="alunos">
                    <ul>
                        {% for aluno in mesas[1] %}
                            <li>{{ aluno }}</li>
                        {% endfor %}
                    </ul>
                </div>
        </div>
        <div class="mesa3">
            <div class="circulo">
                <h2>Mesa 3</h2>
            </div>
            <div class="alunos">
                    <ul>
                        {% for aluno in mesas[2] %}
                            <li>{{ aluno }}</li>
                        {% endfor %}
                    </ul>
                </div>
        </div>
        <div class="mesa4">
            <div class="circulo">
                <h2>Mesa 4</h2>
            </div>
            <div class="alunos">
                    <ul>
                        {% for aluno in mesas[3] %}
                            <li>{{ aluno }}</li>
                        {% endfor %}
                    </ul>
                </div>
        </div>
        <div class="mesa5">
            <div class="circulo">
                <h2>Mesa 5</h2>
            </div>
            <div class="alunos">
                    <ul>
                        {% for aluno in mesas[4] %}
                            <li>{{ aluno }}</li>
                        {% endfor %}
                    </ul>
                </div>
        </div>
        <div class="mesa1">
            <div class="circulo">
                <h2>Mesa 1</h2>
            </div>
            <div class="alunos">
                    <ul>
                        {% for aluno in mesas[0] %}
                            <li>{{ aluno }}</li>
                        {% endfor %}
                    </ul>
                </div>
        </div>
        
    </div>
</body>
<style> 
    .professor{
        grid-area: p;
        background-color: #181848  ;
        margin: 30px;
        margin-right: 0px;
        
    
    }
    .professor h3{
        padding: 20px;
        text-align: center;


    }
    .lousa{
        grid-area: l;
        background-color: #181848  ;
        
    
    }
    .lousa h3{
        padding: 10px;
        text-align: center;
        color: #9eb7cf;


    }
    .vertical-text{
        transform: rotate(270deg); 
        padding: 20px;/* Rotaciona o texto em 90 graus */
        padding-left: 10px;
        font-size: 16px;
        
    }
    body{
        background-color: #9eb7cf;
    }
    h1{
        
        color: #181848 !important;
        text-align: center;
    }
    .grid {
    display: grid;
    grid-template-columns: 130px  auto auto auto; /* Define 5 colunas */
    grid-template-rows: repeat(5, auto); /* Define 5 linhas */
    grid-template-areas:
        "c l l  l"
        "c . .  p"
        "c m1 . m2 "
        "c . m3 . "
        "c m4 . m5";
}

    .corredor{
        background-color: #181848;
        grid-area: c;
        width: 100px;
        margin-right: 30px;        
    } 

    .mesa1{
        display: flex;
        grid-area: m1;
    } 
    .mesa2{
        display: flex;
        grid-area: m2;
    } 
    .mesa3{
        display: flex;
        grid-area: m3;
    } 
    .mesa4{
        display: flex;
        grid-area: m4;
    } 
    .mesa5{
        display: flex;
        grid-area: m5;
    }
    .circulo{
        width: 200px;
        height: 200px;
        border: 3px solid #181848;
        border-radius: 200px;
        
        
    }
    .aluno{
        align-items: end;
        
    }
    h2{
        text-align: center;
        justify-content: center ;
        padding-top: 60px;
    }
</style>
</html>

    '''
    return render_template_string(html_template, mesas=mesas, enumerate=enumerate)
 
if __name__ == '__main__':
    distribuir_alunos()  # Inicializa as mesas na primeira execução
    schedule_task()  # Agenda a tarefa para rodar todos os dias às 6 da manhã
    app.run(host='0.0.0.0', port=5000)
    print("oieee rodei")
Gerenciador de Tarefas em Python
Este projeto é um gerenciador de tarefas simples em Python que permite adicionar, listar, marcar como concluídas, remover e filtrar tarefas por prioridade. As tarefas são salvas em um arquivo JSON para manter a persistência de dados entre as execuções.

Funcionalidades
Adicionar Tarefa: Crie uma nova tarefa com descrição, prazo e prioridade.
Listar Tarefas: Liste as tarefas pendentes ou concluídas.
Marcar como Concluída: Marque uma tarefa específica como concluída.
Remover Tarefa: Remova uma tarefa pendente ou concluída.
Filtrar por Prioridade: Liste tarefas filtrando por prioridade (alta, média ou baixa).
Salvar e Carregar Tarefas: As tarefas são salvas automaticamente em um arquivo JSON.

Como Usar
1. Pré-requisitos
Python 3.6 ou superior.
2. Instalação
Clone o repositório para o seu ambiente local:
git clone https://github.com/seu-usuario/nome-do-repositorio.git

Navegue até o diretório do projeto:
cd nome-do-repositorio

3. Executando o Código
Execute o script test.py:
python test.py

4. Usando o Gerenciador de Tarefas
Para usar as funcionalidades do gerenciador, você pode modificar o código no bloco final de task_manager.py, como no exemplo abaixo:

if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Estudar Python", "2024-11-01", "alta")
    manager.list_tasks()  # Lista todas as tarefas pendentes
    manager.save_tasks()   # Salva as tarefas no arquivo JSON

Comandos Disponíveis
Adicionar Tarefa: manager.add_task("Descrição", "AAAA-MM-DD", "prioridade")
Listar Tarefas: manager.list_tasks(completed=False) para pendentes, manager.list_tasks(completed=True) para concluídas
Marcar como Concluída: manager.mark_task_as_completed(indice)
Remover Tarefa: manager.remove_task(indice)
Filtrar por Prioridade: manager.filter_tasks_by_priority("prioridade")
Salvar Tarefas: manager.save_tasks()
Carregar Tarefas: manager.load_tasks()


Exemplo de Uso:
manager = TaskManager()
manager.add_task("Ler documentação do Python", "2024-11-05", "alta")
manager.add_task("Comprar mantimentos", "2024-10-30", "baixa")
manager.list_tasks()  # Exibe todas as tarefas pendentes
manager.mark_task_as_completed(0)  # Marca a primeira tarefa como concluída
manager.list_tasks(completed=True)  # Lista todas as tarefas concluídas
manager.save_tasks()  # Salva as tarefas no arquivo JSON

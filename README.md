# boradask

POC de processamento em cluster usando [dask](http://dask.pydata.org/)

### Como rodar o POC

```
# Cria a imagem docker
docker build -t dask .

# Cria o container master
docker create -it --name d1 -p 8787:8787 dask

# Cria o container worker
docker create -it --name d2 --link d1:scheduler dask

# Sobe os containers
docker start d1 d2

# Inicia o scheduler no master
docker exec -it d1 dask-scheduler # deixa um terminal rodando isso aqui

# Inicia um worker em cada container
docker exec -it d1 dask-worker localhost:8786 # deixa rodando
docker exec -it d2 dask-worker scheduler:8786 # deixa rodando
```

Nesse ponto vc já pode abrir o browser e deixar preparado pra ficar assistindo a turma trabalhando: http://localhost:8787/status

```
# Taca o pau no processamento distribuido
docker exec -it d1 python primes.py
```


# Instruções

Clone o repositório ou execute pelo git.

Não se esqueça de ter as variáveis de ambiente OPENAI_API_KEY, OPENAI_MODEL e OPENAI_BASE_URL (caso esteja usando um compatível) configuradas.
Você também pode usar outros provedores, como Antrophic e Ollama. Confira a lista aqui:

https://docs.dagger.io/configuration/llm/

Inclusive, é possível usar Docker Model Runner ao invés de Ollama.


# Comandos

```
dagger -m <diretorio clonado, ou o repositório git> call ffmpeg-task --task "<descreva a tarefa que deseja que o agente execute>" --source-Directory-arg <diretório onde estão os arquivos de vídeo ou áudio> export --path <diretório onde você deseja salvar os arquivos>
```

Exemplo:

```
dagger -m ~/Code/Agents/agent-dagger-ffmpeg/ call ffmpeg-task --task "pegue o vídeo que tem p_e_b no nome e extraía o áudio para .mp3 e .ogg nome base do arquivo é áudio, mas extraia apenas os 5 primeiros segundos pro mp3 e 7 segundos pro ogg" --source-Directory-arg . export --path .
```

# Opções adicionais

Se você escrever "dry-run" no prompt, o agente irá criar um arquivo chamado dry-run.txt com os comandos que o agente irá executar, mas não irá executar eles.

*Happy Hacking*

# Tutorial

Confira os vídeos na playlist do meu canal no YouTube:

[Criando um agente FFMPEG com Dagger](https://www.youtube.com/playlist?list=PLqgnlB9wUBbGz5us5B5H_Ot8Zyc1L5tBn)
Stap 1)

Ga in command line naar de map waar de dockerfile staat.

Stap 2)

Run het commando: docker build . -t cloudai_project1_jvc

Stap 3)

Ga naar 'Docker Desktop' en run 'cloudai_project1_jvc'

Stap 4)

Ga naar docker container en run de container opnieuw en in de Logs zie je 
dat de accuracy steeds veranderd. Als je in de files 'workdir_cloud_ai_project1'
download dan zie je dat hier ook het model is opgeslagen. 
(.joblib is niet zichbaar in docker files)


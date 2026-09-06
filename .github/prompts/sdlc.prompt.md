# Persona
 - Especialista em SDLC
 - Especislita em OpenSpec
 - Especialista em OpenSPDD
 - Especialista em Github Copilot 

# Context
Os Agents são necessários atualziarea mas agora nós temos dois frameworks imporatntes agora o OpenSpec e OpenSPDD, isso signfica que ele é um requisito. a metodologia será asim agora
1. Será uma exploração e será disparado o Agente **cobol-vibecoder.agent** e agora ele vai disparar o planejamento
2. O Agente **cobol-planner.agent** vai disparar o OpenSpec e OpenSPDD para gerar o plano de implementação
2.1. opsx-prepose {que foi retoranarndo no resuldo do cobol-vibercoder.agent}
2.2. spdd-analysis /openspec/change/{proposta}
2.3. spdd-reasons-canvas /spdd/analysis/{analysis}
3. O Agente **cobol-coder.agent** vai disparar o OpenSpec e OpenSPDD para gerar o código
3.1. spdd-generate /spdd/prompt/{reasons-canvas}

# instructions

Agora é importaen atualizar os agens e com o fluxo agora usando o openspec e openspdd.

[0] explorar -> [1] propose -> [1] analysis -> [1]reasons-canvas -> [2]generate

cobol-vibercoder -> cobol-planner -> cobol-coder


# output

agents/*
skills/*
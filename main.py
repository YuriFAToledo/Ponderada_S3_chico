from fpdf import FPDF

# Criando o PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Título
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, "Análise de Dashboard: LLM-Stats", ln=True, align='C')
pdf.ln(10)

# Introdução e Escolha do Caso
pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, "1. Introdução e Escolha do Caso", ln=True)
pdf.set_font("Arial", size=12)
intro_text = (
    "O avanço dos modelos de inteligência artificial tornou essencial a comparação entre diferentes Large Language Models (LLMs). "
    "O site LLM-Stats apresenta uma solução inovadora ao consolidar benchmarks de IA em uma única dashboard. "
    "Esta análise explora como esse dashboard organiza e apresenta os dados e como ele se compara a outras abordagens, como a da xAI."
)
pdf.multi_cell(0, 8, intro_text)
pdf.ln(5)

# Problema e Contexto
pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, "2. Problema e Contexto", ln=True)
pdf.set_font("Arial", size=12)
context_text = (
    "A crescente diversidade de modelos de IA criou um desafio para pesquisadores e empresas: comparar diferentes modelos de forma justa. "
    "Benchmarks padronizados são essenciais para avaliar o desempenho real dos LLMs. "
    "Dashboards que apresentam dados de forma transparente e intuitiva são ferramentas fundamentais para facilitar essa análise."
)
pdf.multi_cell(0, 8, context_text)
pdf.ln(5)

# Descrição da Solução
pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, "3. Descrição da Solução: LLM-Stats", ln=True)
pdf.set_font("Arial", size=12)
solution_text = (
    "O LLM-Stats se destaca por sua abordagem transparente e detalhada. "
    "Ele apresenta rankings de modelos com métricas diversas, utilizando gráficos absolutos que evitam manipulação de dados."
)
pdf.multi_cell(0, 8, solution_text)
pdf.ln(5)

# Adicionando gráficos analisados
pdf.image("./img_5.png", x=10, w=180)  # GPQA Leaderboard
pdf.ln(5)

pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, "GPQA Leaderboard", ln=True)
pdf.set_font("Arial", size=12)
gpqa_text = (
    "O gráfico GPQA Leaderboard apresenta a performance dos modelos em questões científicas complexas. "
    "A escolha de um gráfico de barras horizontais facilita a comparação direta entre os modelos. "
    "A escala absoluta utilizada mantém a transparência dos dados, evitando distorções."
)
pdf.multi_cell(0, 8, gpqa_text)
pdf.ln(5)

pdf.image("img_6.png", x=10, w=180)  # MATH Leaderboard
pdf.ln(5)

pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, "MATH Leaderboard", ln=True)
pdf.set_font("Arial", size=12)
math_text = (
    "Este gráfico avalia a habilidade dos LLMs em resolver problemas matemáticos. "
    "A escolha de barras coloridas para cada modelo auxilia na distinção rápida das performances. "
    "A estrutura bem definida permite uma interpretação rápida dos resultados."
)
pdf.multi_cell(0, 8, math_text)
pdf.ln(5)

pdf.image("img_2.png", x=10, w=180)  # Evolução Temporal
pdf.ln(5)

pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, "Evolução Temporal dos Modelos", ln=True)
pdf.set_font("Arial", size=12)
evol_text = (
    "O gráfico de linha ilustra a evolução da performance dos modelos ao longo do tempo. "
    "Ele permite uma visão clara do progresso e das tendências do setor, sendo um diferencial do LLM-Stats."
)
pdf.multi_cell(0, 8, evol_text)
pdf.ln(5)

# Comparação com xAI
pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, "4. Comparação com xAI (Grok-3)", ln=True)
pdf.set_font("Arial", size=12)
xai_text = (
    "Diferente do LLM-Stats, a xAI utilizou um gráfico recortado para enfatizar a superioridade do Grok-3. "
    "Ao omitir a parte inferior do gráfico, a empresa gerou um efeito visual exagerado, distorcendo a percepção dos dados."
)
pdf.multi_cell(0, 8, xai_text)
pdf.ln(5)

pdf.image("img_7.png", x=10, w=180)  # Gráfico xAI Grok-3
pdf.ln(5)

# Análise Crítica
pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, "5. Análise Crítica: Transparência e Eficiência", ln=True)
pdf.set_font("Arial", size=12)
analysis_text = (
    "O LLM-Stats acerta ao apresentar dados com clareza e sem manipulações. "
    "Seu uso de gráficos bem organizados e cores distintas facilita a leitura e a tomada de decisões. "
    "A comparação com a xAI reforça a importância da escala absoluta para evitar distorções visuais."
)
pdf.multi_cell(0, 8, analysis_text)
pdf.ln(5)

# Conclusão
pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, "6. Conclusão", ln=True)
pdf.set_font("Arial", size=12)
conclusion_text = (
    "O LLM-Stats se destaca como um dashboard confiável e transparente para avaliação de LLMs. "
    "Sua abordagem gráfica bem fundamentada facilita a análise comparativa e se alinha às boas práticas descritas na Aela.io."
)
pdf.multi_cell(0, 8, conclusion_text)
pdf.ln(5)

# Referências
pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, "Referências", ln=True)
pdf.set_font("Arial", size=12)
references_text = (
    "- https://llm-stats.com/\n"
    "- https://www.aela.io/pt-br/blog/conteudos/dashboard-como-criar-o-design-de-dados-e-informacoes\n"
    "- Análise comparativa de dashboards e visualização de dados em inteligência artificial."
)
pdf.multi_cell(0, 8, references_text)

# Salvar PDF
pdf_output_path = "./analise_dashboard_llm_stats_completa.pdf"
pdf.output(pdf_output_path)

# Retornar caminho do PDF gerado
pdf_output_path

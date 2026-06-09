import pandas as pd
import os

def carregar_dados(caminho_arquivo):
    """Carrega a planilha de projetos elétricos."""
    if os.path.exists(caminho_arquivo):
        df = pd.read_csv(caminho_arquivo)
        # ESTA LINHA ABAIXO REMOVE ESPAÇOS INVISÍVEIS DOS CABEÇALHOS:
        df.columns = df.columns.str.strip()
        return df
    else:
        raise FileNotFoundError(f"Arquivo não encontrado em: {caminho_arquivo}")

def auditar_prazos_ren1000(df):
    """
    Aplica as regras de negócio baseadas na REN 1000/2021 da ANEEL.
    Verifica se os dias decorridos estouraram o limite regulatório.
    """
    # Cria uma nova coluna de status comparando os dias reais com o limite da norma
    df['Status_Auditoria'] = df.apply(
        lambda row: '⚠️ ESTOURADO' if row['dias_corridos'] > row['limite_regulatorio'] else '✅ EM CONFORMIDADE',
        axis=1
    )
    
    # Calcula o desvio (quantos dias passou do prazo regulamentar)
    df['Dias_Desvio'] = df['dias_corridos'] - df['limite_regulatorio']
    df['Dias_Desvio'] = df['Dias_Desvio'].apply(lambda x: x if x > 0 else 0)
    
    return df

def gerar_relatorio_alertas(df):
    """Filtra apenas os projetos que estão irregulares para a gestão atuar."""
    projetos_criticos = df[df['Status_Auditoria'] == '⚠️ ESTOURADO']
    
    print("\n" + "="*50)
    print("   RELATÓRIO DE AUDITORIA - ENGENHARIA 4.0 (ANEEL)   ")
    print("="*50)
    print(f"Total de projetos analisados: {len(df)}")
    print(f"Projetos com prazo estourado: {len(projetos_criticos)}")
    print("-"*50)
    
    if not os.path.exists('outputs'):
         os.makedirs('outputs')
         
    if len(projetos_criticos) > 0:
        print("\n🚨 PROJETOS CRÍTICOS ENCONTRADOS:")
        print(projetos_criticos[['id_projeto', 'tipo_solicitacao', 'fase_atual', 'dias_corridos', 'Dias_Desvio']])
        
        # Exporta automaticamente para um novo CSV de auditoria
        projetos_criticos.to_csv('outputs/alertas_auditoria.csv', index=False)
        print("\n💾 Arquivo 'outputs/alertas_auditoria.csv' gerado com sucesso para a gerência.")
    else:
        print("\n🎉 Todos os projetos estão em conformidade com a REN 1000/2021!")
    print("="*50 + "\n")

if __name__ == "__main__":
    # Caminho relativo para a base de dados
    caminho_base = os.path.join('data', 'projetos_teste.csv')
    
    try:
        # Execução do pipeline de dados
        dados_projetos = carregar_dados(caminho_base)
        dados_auditados = auditar_prazos_ren1000(dados_projetos)
        gerar_relatorio_alertas(dados_auditados)
        
    except Exception as e:
        print(f"Erro na execução do pipeline: {e}")
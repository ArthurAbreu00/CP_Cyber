# ClickSeguro — Demo vulnerável para testes com OWASP ZAP

Pequena aplicação Flask (porta `8080`) intencionalmente vulnerável a **Reflected XSS** para uso em testes/CI com OWASP ZAP.

# Como rodar (local)
`bash
# torne executável se necessário
chmod +x start-app.sh

# rodar a app
./start-app.sh
# ou: python3 app.py
Acesse: http://localhost:8080

Teste rápido (XSS)

No formulário /login envie no campo Usuário:

<script>alert('XSS')</script>


O script será refletido na resposta (comportamento proposital).

Integração CI

Inclui workflow de exemplo em .github/workflows/zap-scan.yml que:

inicia a app no runner,

executa zap-baseline.py (container oficial ZAP),

gera zap-report.html e zap-report.json,

falha o job se houver alertas High ou Critical,

salva os relatórios como artifact.

# Bit-OS

> Uma distribuição **Rolling Release** baseada em **Gentoo Linux**, focada em performance máxima, simplicidade e automação total. Desenvolvido e mantido pela **Next Level Software Studio**.

O **Bit-OS** oferece a robustez do Gentoo com a simplicidade e leveza do **OpenRC**, entregando um sistema otimizado que respeita a privacidade e o controle total do utilizador sobre o hardware.

---

## 🌍 Idiomas Suportados

O instalador e o sistema configuram nativamente as localidades e teclados para:
* 🇵🇹 **Português** (pt-PT)
* 🇩🇪 **Alemão** (de-DE)
* 🇫🇷 **Francês** (fr-FR)
* 🇺🇸 **Inglês** (en-US)

---

## 💻 Requisitos Mínimos Recomendados

| Componente | Requisito Mínimo |
| :--- | :--- |
| **Armazenamento** | **80 GiB** de espaço livre (SSD recomendado) |
| **Memória RAM** | **2 GB** (para processos de compilação básicos) |
| **Processador** | Arquitetura 64-bit (**AMD64** ou **ARM64**) |
| **Conectividade** | Internet estável (necessária para instalação e atualizações mensais) |

---

## 🏗️ Arquiteturas Suportadas

O Bit-OS deteta e aplica otimizações de compilação (`CFLAGS` e `CPU_FLAGS`) de acordo com a arquitetura:

* **AMD64 (x86_64):** Focado em processadores modernos, utilizando o perfil `x86-64-v3` para aproveitar instruções como AVX2 e BMI.
* **ARM64 (AArch64):** Suporte genérico para processadores ARM de 64 bits, garantindo estabilidade em servidores e SBCs.

---

## 🔌 Hardware Específico Suportado

Diferente de uma instalação genérica, o Bit-OS possui suporte dedicado para:

### **Raspberry Pi 5**
* **Kernel:** Otimizado para o SoC **BCM2712**.
* **Firmware:** Inclusão automática dos blobs e bootloader oficiais da RPi Foundation.
* **Gráficos:** Suporte nativo para aceleração de hardware via driver **V3D**.
* **CPU:** Micro-otimizações para os núcleos **Cortex-A76**.

### **PC Genérico (Laptop/Desktop)**
* Suporte abrangente para drivers Wi-Fi modernos, GPUs (Intel/AMD/Nvidia) e gestão de energia via OpenRC.

---

## 🚀 Guia de Instalação

A instalação deve ser feita a partir do ambiente oficial **Gentoo Minimal Installation CD**.
Nota: use o correto para a arquitetura da sua CPU.

### 1. Preparação
Dê boot com a ISO oficial do Gentoo e ligue-se à internet.

### 2. Execução
O Bit-OS automatiza o particionamento, a extração do Stage3, a compilação do Kernel e a configuração final. Corra o comando:

```bash
wget
chmod +x installer.sh
./installer.sh
```

Aviso: O script é auto-suficiente. Ele finalizará a instalação, desmontará as partições e reiniciará o sistema automaticamente quando terminar.

⚙️ Filosofia e Manutenção

- **OpenRC Nativo:** O Bit-OS suporta apenas o OpenRC. Não há suporte para Systemd, garantindo um sistema minimalista e scripts de inicialização legíveis.
- **Rolling Release:** O sistema atualiza-se continuamente. Não existem "versões fixas", apenas o estado mais recente dos repositórios.
- **Downgrades via Git:** Como o GitHub guarda todo o histórico, é possível reverter o instalador para versões anteriores. No entanto, a Next Level Software Studio não recomenda esta prática em sistemas já instalados devido ao risco de quebra de dependências binárias.

## 📦 Gestão de Pacotes
O Bit-OS utiliza o bpm (Bit-OS Package Manager). Este gestor foi construído como uma camada de abstração sobre o Portage, simplificando a sintaxe e automatizando tarefas comuns de manutenção sem sacrificar a flexibilidade do Gentoo.

## 📜 Licença e Propriedade Intelectual
A licença está disponível em: https://raw.githubusercontent.com/NextLevelSoftwareStudio/Bit-OS/refs/heads/main/LICENSE
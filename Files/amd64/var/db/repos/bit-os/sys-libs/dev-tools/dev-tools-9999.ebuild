# Copyright 1999-2026 Bit-OS Team
# Distributed under the terms of the GNU General Public License v2

EAPI=8

DESCRIPTION="Ferramentas de desenvolvimento do Bit-OS"
HOMEPAGE="https://bit-os.org"

LICENSE="GPL-2"
SLOT="0"
KEYWORDS="~amd64"

SRC_URI="" # Código local na pasta files/, não há download externo

S="${WORKDIR}/${P}"

src_unpack() {
	# Cria o diretório de trabalho limpo
	mkdir -p "${S}" || die
	
	# Copia o Makefile e as pastas de código para o diretório de compilação
	cp "${FILESDIR}/Makefile" "${S}/" || die
	cp -R "${FILESDIR}/src" "${S}/" || die
	cp -R "${FILESDIR}/include" "${S}/" || die
}

src_compile() {
	emake
}

src_install() {
	# 1. Executa a instalação padrão do seu Makefile 
	# (que deve jogar os arquivos em ${D}/usr/lib64/bit-os/dev-tools)
	emake DESTDIR="${D}" install

	# 2. Cria um arquivo temporário de ambiente
	# O número 99 define a prioridade de leitura do arquivo
	echo "LDPATH=\"/usr/lib64/bit-os/dev-tools\"" > "${T}/99bit-os"

	# 3. Instala o arquivo de ambiente no sistema de destino
	doenvd "${T}/99bit-os"
	einfo "Instalation complete."
}
# INSTALL
apt update -y
apt upgrade -y
apt install python3 --upgrade
git clone https://github.com/Agent-Razzo/cpf-valid/
cd cpf-valid
python valid.py <cpf>

#!/bin/bash

# Install Python and pip
apt-get update
apt-get install -y python3 python3-pip

# Install dependencies
pip install -r requirements.txt

# Create a simple wrapper to run your Streamlit app
echo '#!/bin/sh' > run.sh
echo 'streamlit run app.py --server.address=0.0.0.0 --server.port=$PORT' >> run.sh
chmod +x run.sh

# Create a Procfile for Cloudflare Workers
echo 'web: ./run.sh' > Procfile
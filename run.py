import os
from project import main

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    main.app.run(host='127.0.0.1', port=port)
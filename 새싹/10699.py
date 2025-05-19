# YYYY-MM-DD
import datetime
print(str(datetime.datetime.now())[0:10])

# - [] 도대체 이게 왜 실패인가?

from datetime import datetime
now = datetime.now().date()
print(now)

# - [] 도대체 왜 이게 맞는가?
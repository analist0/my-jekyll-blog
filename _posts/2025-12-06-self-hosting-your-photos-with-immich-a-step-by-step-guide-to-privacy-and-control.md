---
layout: unified-post
title: "Self-Hosting Your Photos with Immich: A Step-by-Step Guide to Privacy and Control"
description: "מדריך מקיף ומפורט על Self-Hosting Your Photos with Immich: A Step-by-Step Guide to Privacy and Control. כולל הסברים צעד-אחר-צעד, דוגמאות קוד, שיטות עבודה מומלצות ומקרי שימוש מהעולם האמיתי."
date: 2025-12-06 09:24:03 +0200
categories: ['Tutorial', 'Development']
tags: ['self', 'hosting', 'your', 'photos', 'with', 'immich']
author: "Tech Insights"
lang: he
---

---
layout: post
title: "Self-Hosting Your Photos with Immich: A Step-by-Step Guide to Privacy and Control"
date: 2023-10-10
categories: [טכנולוגיה, אבטחת מידע, פיתוח תוכנה]
tags: [Immich, self-hosting, privacy, photography, Docker, Kubernetes, Python, JavaScript, Bash]
author: TechWriter
---

# 🖼️ Self-Hosting Your Photos with Immich: מדריך מקיף צעד-אחר-צעד לפרטיות ושליטה

## הקדמה

בעידן הדיגיטלי של היום, שמירת תמונות והזכרונות שלנו בשירותי ענן חיצוניים הפכה להיות הנורמה. עם זאת, עבור אלו המעוניינים בשליטה מלאה על הנתונים שלהם ובפרטיות מרבית, self-hosting הוא הפתרון האידיאלי. בשנים האחרונות, פתרונות כמו Immich התחילו לצבור תאוצה בקרב קהילת המפתחים והמשתמשים הפרטיים כאחד.

Immich הוא פתרון קוד פתוח לניהול תמונות שמאפשר לך לאחסן, לסנן ולשתף את התמונות שלך בצורה מאובטחת ופרטית. בניגוד לשירותי ענן מסחריים, עם Immich אתה יכול להתקין את השרת שלך על ההתקן שלך, מה שמעניק לך שליטה מלאה על הנתונים שלך.

במדריך זה, נסקור בצורה מפורטת את הדרך להטמעת Immich, החל מדרישות מוקדמות ועד להתקנה מתקדמת ושימוש בתכונות מתקדמות. נכסה גם את השיטות העבודה המומלצות, המלכודות הנפוצות וטכניקות מתקדמות שישפרו את חוויית המשתמש שלך.

### מקרי שימוש

- **משפחות**: שמירה ושיתוף תמונות משפחתיות בצורה מאובטחת.
- **צלמים מקצועיים**: ניהול גלריות תמונות בצורה פרטית ומאורגנת.
- **חובבי פרטיות**: אלו המעוניינים לשמור את הנתונים שלהם מחוץ לשירותי ענן ציבוריים.
- **מפתחים**: התנסות והתאמה של פתרון קוד פתוח לצרכים ספציפיים.

## דרישות מוקדמות וכלים נדרשים

לפני שנתחיל בהתקנת Immich, חשוב להבין את הדרישות המוקדמות והכלים הנדרשים. להלן רשימה מפורטת:

### חומרה

- **מעבד**: לפחות Intel Core i3 או שווה ערך.
- **זכרון**: לפחות 4GB RAM, מומלץ 8GB ומעלה.
- **אחסון**: לפחות 50GB של חלל אחסון פנוי, תלוי בכמות התמונות שלך.

### תוכנה

- **מערכת הפעלה**: תומך ב-Linux, macOS ו-Windows.
- **Docker**: גרסה 20.10 ומעלה.
- **Docker Compose**: גרסה 1.29 ומעלה.
- **git**: לצורך הורדת קוד ממאגרי קוד.

### כלים נוספים

- **טרמינל/קונסולה**: להרצת פקודות.
- **עורך טקסט**: לשינוי קבצי קונפיגורציה.
- **דפדפן אינטרנט**: לגישה ל-UI של Immich.

## הטמעה צעד-אחר-צעד עם דוגמאות קוד

### שלב 1: התקנת Docker ו-Docker Compose

השלב הראשון בהטמעת Immich הוא התקנת Docker ו-Docker Compose. להלן הפקודות להתקנה ב-Linux (Ubuntu/Debian):

```bash
# התקנת Docker
sudo apt-get update
sudo apt-get install -y docker.io

# התקנת Docker Compose
sudo apt-get install -y docker-compose
```

ב-macOS, תוכל להתקין Docker Desktop מהאתר הרשמי של Docker. ב-Windows, התקן את Docker Desktop ל-Windows.

### שלב 2: הורדת קוד Immich

כדי להוריד את קוד המקור של Immich, השתמש בפקודה הבאה:

```bash
# הורדת קוד ממאגר GitHub
git clone https://github.com/immich-app/immich.git
cd immich
```

### שלב 3: התקנת Immich באמצעות Docker Compose

בתיקיית `immich`, תמצא קובץ בשם `docker-compose.yml`. זהו הקובץ שמגדיר את כל השירותים הדרושים להרצת Immich. להלן דוגמה לקובץ `docker-compose.yml` מותאם:

```yaml
version: '3'

services:
  immich-server:
    image: ghcr.io/immich-app/immich-server:${IMMICH_VERSION:-release}
    container_name: immich_server
    volumes:
      - ${UPLOAD_LOCATION}:/usr/src/app/upload
    environment:
      - DB_HOSTNAME=immich_database
      - DB_USERNAME=${DB_USERNAME:-immich}
      - DB_PASSWORD=${DB_PASSWORD:-immich}
      - DB_DATABASE_NAME=${DB_DATABASE_NAME:-immich}
      - JWT_SECRET=${JWT_SECRET:-secret}
      - MAPBOX_TOKEN=${MAPBOX_TOKEN:-}
    depends_on:
      - immich_database
    restart: always

  immich-database:
    image: postgres:14-alpine
    container_name: immich_database
    volumes:
      - ${DB_DATA_LOCATION}:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=${DB_USERNAME:-immich}
      - POSTGRES_PASSWORD=${DB_PASSWORD:-immich}
      - POSTGRES_DB=${DB_DATABASE_NAME:-immich}
    restart: always

  immich-redis:
    image: redis:6-alpine
    container_name: immich_redis
    restart: always

  immich-machine-learning:
    image: ghcr.io/immich-app/immich-machine-learning:${IMMICH_VERSION:-release}
    container_name: immich_machine_learning
    volumes:
      - ${UPLOAD_LOCATION}:/usr/src/app/upload
    environment:
      - IMMICH_SERVER_URL=http://immich-server:3001
    depends_on:
      - immich-server
    restart: always
```

כדי להריץ את Immich, השתמש בפקודה הבאה:

```bash
# הרצת Immich באמצעות Docker Compose
docker-compose up -d
```

### שלב 4: גישה ל-UI של Immich

לאחר שהרצת את Immich, תוכל לגשת ל-UI שלו באמצעות הדפדפן שלך. הכתובת הבסיסית היא `http://localhost:3000`. אם אתה משתמש בשרת מרוחק, החלף את `localhost` בכתובת ה-IP של השרת שלך.

### שלב 5: התקנת תלויות נוספות

Immich תומך בתכונות מתקדמות כמו זיהוי פנים ומיון תמונות באמצעות בינה מלאכותית. כדי להפעיל את התכונות הללו, תצטרך להתקין תלויות נוספות כמו TensorFlow ו-OpenCV. להלן דוגמה להתקנת התלויות הללו ב-Python:

```python
# התקנת TensorFlow ו-OpenCV
import subprocess

# התקנת TensorFlow
subprocess.check_call([sys.executable, "-m", "pip", "install", "tensorflow"])

# התקנת OpenCV
subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
```

## שיטות עבודה מומלצות וטיפים

כדי להבטיח שההתקנה שלך תהיה יציבה ומאובטחת, חשוב להקפיד על שיטות עבודה מומלצות. להלן כמה טיפים חשובים:

### שימוש ב-Docker Volumes

שימוש ב-Docker Volumes יעזור לך לשמור את הנתונים שלך גם אם תצטרך להתקין מחדש את Immich. דוגמה לשימוש ב-Docker Volumes בקובץ `docker-compose.yml`:

```yaml
version: '3'

services:
  immich-server:
    ...
    volumes:
      - immich_data:/usr/src/app/upload

volumes:
  immich_data:
```

### עדכוני אבטחה

הקפד לעדכן את Immich ואת התלויות שלו באופן קבוע כדי להבטיח את האבטחה של המערכת שלך. דוגמה לפקודת עדכון:

```bash
# עדכון Immich
docker-compose pull
docker-compose up -d
```

### גיבויים

בצע גיבויים קבועים של הנתונים שלך. דוגמה לפקודת גיבוי ב-Bash:

```bash
# גיבוי נתונים
tar -czvf immich_backup.tar.gz /path/to/immich_data
```

### שימוש ב-HTTPS

כדי להגן על התקשורת בין הדפדפן ל-Immich, השתמש ב-HTTPS. דוגמה להתקנת Let's Encrypt עבור HTTPS:

```bash
# התקנת Certbot
sudo apt-get install certbot

# יצירת תעודת HTTPS
sudo certbot certonly --standalone -d example.com

# הוספת תעודת HTTPS ל-Docker Compose
echo "version: '3'

services:
  immich-server:
    ...
    ports:
      - '443:3000'
    environment:
      - HTTPS=true
      - SSL_CERT_PATH=/etc/letsencrypt/live/example.com/fullchain.pem
      - SSL_KEY_PATH=/etc/letsencrypt/live/example.com/privkey.pem
    volumes:
      - /etc/letsencrypt:/etc/letsencrypt:ro
" > docker-compose.yml
```

## מלכודות נפוצות ואיך להימנע מהן

כמו בכל פרויקט, גם ב-Immich יש כמה מלכודות נפוצות שחשוב להכיר ולדעת כיצד להימנע מהן. להלן כמה מהמלכודות הנפוצות ופתרונות להן:

### בעיות בהתקנה

אם אתה נתקל בבעיות במהלך ההתקנה, ודא שהתקנת את כל הדרישות המוקדמות ושיש לך הרשאות ניהול מתאימות. דוגמה לבדיקת הרשאות:

```bash
# בדיקת הרשאות
ls -la /path/to/immich_data
```

### בעיות בביצועים

אם אתה חווה בעיות בביצועים, ודא שהחומרה שלך עומדת בדרישות המינימליות ושקבצי התמונות שלך מאורגנים כראוי. דוגמה לבדיקת ביצועים:

```bash
# בדיקת שימוש בזכרון
docker stats

# בדיקת שימוש בדיסק
df -h
```

### בעיות בזיהוי פנים

אם זיהוי הפנים לא עובד כראוי, ודא שהתקנת את כל התלויות הנדרשות ושהתמונות שלך בפורמטים נתמכים. דוגמה לבדיקת תלויות:

```python
# בדיקת התקנת TensorFlow
import tensorflow as tf
print(tf.__version__)

# בדיקת התקנת OpenCV
import cv2
print(cv2.__version__)
```

## טכניקות מתקדמות

כדי לנצל את מלוא הפוטנציאל של Immich, חשוב להכיר כמה טכניקות מתקדמות. להלן כמה מהן:

### שימוש ב-Kubernetes

אם אתה משתמש בסביבת Kubernetes, תוכל להתקין את Immich באמצעות Helm. דוגמה לקובץ `values.yaml`:

```yaml
# values.yaml
replicaCount: 1

image:
  repository: ghcr.io/immich-app/immich-server
  tag: release
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 3000

ingress:
  enabled: true
  className: ""
  annotations: {}
    # kubernetes.io/ingress.class: nginx
    # kubernetes.io/tls-acme: "true"
  hosts:
    - host: immich.example.com
      paths:
        - path: /
          pathType: ImplementationSpecific
  tls: []
  #  - secretName: immich-tls
  #    hosts:
  #      - immich.example.com

resources: {}
  # We usually recommend not to specify default resources and to leave this as a conscious
  # choice for the user. This also increases chances charts run on environments with little
  # resources, such as Minikube. If you do want to specify resources, uncomment the following
  # lines, adjust them as necessary, and remove the curly braces after 'resources:'.
  # limits:
  #   cpu: 100m
  #   memory: 128Mi
  # requests:
  #   cpu: 100m
  #   memory: 128Mi

nodeSelector: {}

tolerations: []

affinity: {}
```

דוגמה להתקנת Immich באמצעות Helm:

```bash
# הוספת repo של Helm
helm repo add immich https://charts.immich.app

# התקנת Immich
helm install immich immich/immich -f values.yaml
```

### שימוש ב-API של Immich

Immich מספק API שמאפשר לך לבצע פעולות מתקדמות. דוגמה לשימוש ב-API ב-JavaScript:

```javascript
// שימוש ב-API של Immich
const axios = require('axios');

const API_URL = 'http://localhost:3001/api';
const API_KEY = 'your_api_key';

// פונקציה לשליפת כל התמונות
async function getPhotos() {
  try {
    const response = await axios.get(`${API_URL}/photos`, {
      headers: {
        'Authorization': `Bearer ${API_KEY}`
      }
    });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

// פונקציה להעלאת תמונה חדשה
async function uploadPhoto(filePath) {
  try {
    const formData = new FormData();
    formData.append('file', fs.createReadStream(filePath));

    const response = await axios.post(`${API_URL}/photos`, formData, {
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'multipart/form-data'
      }
    });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

// שימוש בפונקציות
getPhotos();
uploadPhoto('/path/to/photo.jpg');
```

### שימוש ב-Webhooks

Immich תומך ב-Webhooks, מה שמאפשר לך לקבל התראות על אירועים שונים. דוגמה להגדרת Webhook:

```bash
# הגדרת Webhook
curl -X POST \
  http://localhost:3001/api/webhooks \
  -H 'Authorization: Bearer your_api_key' \
  -H 'Content-Type: application/json' \
  -d '{
    "event": "photo.uploaded",
    "url": "https://your-webhook-url.com"
  }'
```

## דוגמאות מהעולם האמיתי

כדי להמחיש את השימוש ב-Immich, להלן כמה דוגמאות מהעולם האמיתי:

### דוגמה 1: משפחה שמשתמשת ב-Immich

משפחה ממוצעת עם ילדים קטנים מעוניינת לשמור ולשתף תמונות משפחתיות בצורה מאובטחת. הם מחליטים להתקין את Immich על שרת ביתי ולשתף את הגישה לכל בני המשפחה. הם משתמשים ב-API של Immich כדי ליצור אפליקציה פשוטה שמאפשרת לכל בן משפחה להעלות תמונות ולצפות בתמונות של אחרים.

### דוגמה 2: צלם מקצועי

צלם מקצועי מעוניין לנהל את הגלריות שלו בצורה מאובטחת ומאורגנת. הוא מחליט להשתמש ב-Immich כדי לאחסן את התמונות שלו ולהשתמש בתכונות המיון והזיהוי שלו כדי לארגן את התמונות לפי אירועים ונושאים. הוא גם משתמש ב-API של Immich כדי ליצור אתר אינטרנט שבו הוא יכול לשתף את התמונות שלו עם לקוחותיו.

### דוגמה 3: חובב פרטיות

חובב פרטיות מעוניין לשמור את הנתונים שלו מחוץ לשירותי ענן ציבוריים. הוא מחליט להתקין את Immich על שרת פרטי ולהשתמש בו כדי לאחסן את כל התמונות שלו. הוא משתמש ב-HTTPS ובגיבויים קבועים כדי להבטיח את האבטחה של הנתונים שלו.

## סיכום וצעדים הבאים

במדריך זה, סקרנו בצורה מפורטת את הדרך להטמעת Immich, החל מדרישות מוקדמות ועד להתקנה מתקדמת ושימוש בתכונות מתקדמות. כיסינו גם את השיטות העבודה המומלצות, המלכודות הנפוצות וטכניקות מתקדמות שישפרו את חוויית המשתמש שלך.

הצעדים הבאים שלך יכולים לכלול:

- **התאמה אישית**: התאם את Immich לצרכים הספציפיים שלך על ידי שינוי קבצי קונפיגורציה ושימוש ב-API.
- **אינטגרציה**: שתף את התמונות שלך עם אפליקציות אחרות באמצעות Webhooks ו-API.
- **אבטחה**: הקפד לעדכן את Immich ואת התלויות שלו באופן קבוע ולבצע גיבויים קבועים.

אם יש לך שאלות נוספות או שאתה זקוק לעזרה נוספת, אל תהסס לפנות לקהילת Immich ב-GitHub או בפורומים הרלוונטיים.

בהצלחה!

---

### מטא-דאטה

**תגיות**: Immich, self-hosting, privacy, photography, Docker, Kubernetes, Python, JavaScript, Bash

**מילות מפתח**: Immich, self-hosting, פרטיות, צילום, Docker, Kubernetes, Python, JavaScript, Bash, התקנה, אבטחה, ביצועים, זיהוי פנים, API, Webhooks
# Guía de Ejecución - Obligatorio AWS EKS

Este documento explica cómo ejecutar el sistema completo utilizando Docker, Amazon ECR y Kubernetes en AWS EKS.

---

## 1. Construcción de las Imágenes Docker

### Backend (users-api)
```bash
cd backend
docker build -t users-api .
```

### Frontend
```bash
cd frontend
docker build -t frontend .
```

### Notifier
```bash
cd notifier
docker build -t notifier .
```

---

## 2. Autenticación en Amazon ECR

```bash
ACCOUNT_ID=580248541584
REGION=us-east-1
ECR="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"

aws ecr get-login-password --region $REGION   | docker login --username AWS --password-stdin $ECR
```

---

## 3. Subir Imágenes a ECR

### Backend
```bash
docker tag users-api:latest $ECR/users-api:v1
docker push $ECR/users-api:v1
```

### Frontend
```bash
docker tag frontend:latest $ECR/frontend:latest
docker push $ECR/frontend:latest
```

### Notifier
```bash
docker tag notifier:latest $ECR/notifier:latest
docker push $ECR/notifier:latest
```

---

## 4. Conectar la EC2 al Clúster EKS

```bash
aws eks --region us-east-1 update-kubeconfig --name las-flipantes-agrupaciones-de-recursos-computacionales
kubectl cluster-info
kubectl get nodes
```

---

## 5. Despliegue en Kubernetes

```bash
kubectl apply -f k8s-obligatorio.yaml
kubectl get pods -n app-lab
kubectl get svc -n app-lab
```

---

## 6. Migraciones del Backend Django

```bash
kubectl exec -it -n app-lab users-api-XXXXX -- python manage.py migrate
```

Reemplace `XXXXX` por el nombre real del pod.

---

## 7. Acceso al Sistema

1. Obtener el LoadBalancer:
   ```bash
   kubectl get svc -n app-lab
   ```
2. Abrir el `EXTERNAL-IP` del servicio frontend.

---

## 8. Ver Logs

### Backend
```bash
kubectl logs -n app-lab users-api-XXXXX
```

### Notifier
```bash
kubectl logs -n app-lab notifier-XXXXX
```

---

## 9. Eliminar Recursos

```bash
kubectl delete -f k8s-obligatorio.yaml
```

---

## FIN
Este archivo demuestra cómo ejecutar, desplegar y probar la aplicación completa en AWS EKS.

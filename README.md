# pytorch_install_manual

---

# PyTorch 설치

본 프로젝트에서는 PyTorch 1.12.0 버전을 사용하며, CUDA 버전은 11.6입니다. 리눅스 운영체제의 버전은 Ubuntu 18.04입니다.

## CUDA 설치

먼저, 현재 시스템에 설치된 CUDA 버전을 확인합니다. 터미널에서 다음 명령어를 실행합니다.

```bash
nvidia-smi
```

만약 설치된 CUDA 버전이 11.6이 아닌 경우, CUDA 11.6 버전을 설치해야 합니다. 설치 방법은 NVIDIA의 공식 페이지를 참고하십시오.

## PyTorch 설치

아래의 명령어를 터미널에 입력하여 PyTorch를 설치합니다.

```bash
conda install pytorch==1.13.0 torchvision==0.14.0 torchaudio==0.13.0 pytorch-cuda=11.6 -c pytorch -c nvidia
```

위 명령어는 PyTorch 1.13.0 버전 및 해당 버전에 맞는 torchvision, torchaudio를 설치합니다. 또한, CUDA 버전을 11.6으로 지정하여 pytorch-cuda가 해당 버전에 맞게 설치됩니다.

## PyTorch 설치 확인

PyTorch가 제대로 설치되었는지 확인하기 위해 Python 인터프리터를 실행시킨 후, 다음 코드를 실행합니다.

```python
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)

# 출력 예시
# PyTorch version: 1.12.0
# CUDA available: True
# CUDA version: 11.6
# Linux version: Ubuntu 18.04
```

위 코드 실행 결과로 PyTorch 버전, CUDA 사용 가능 여부, CUDA 버전 및 리눅스 버전이 정상적으로 출력되어야 합니다.

---

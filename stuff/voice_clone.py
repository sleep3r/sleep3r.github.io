#!/usr/bin/env python3
import os
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel


def main() -> None:
    # Device selection (MPS on Apple Silicon)
    if torch.backends.mps.is_available():
        device = "mps"
        print("✅ Используется MPS (Apple Silicon)")
    else:
        device = "cpu"
        print("⚠️ Используется CPU (MPS недоступен)")

    print(f"PyTorch версия: {torch.__version__}")
    print(f"Устройство: {device}")

    # Paths
    desktop_path = os.path.expanduser("~/Desktop")
    ref_audio_path = os.path.join(desktop_path, "один два три.mov")

    if not os.path.exists(ref_audio_path):
        fallback = os.path.join(desktop_path, "123.mov")
        if os.path.exists(fallback):
            print(f"⚠️ Файл не найден: {ref_audio_path}")
            print(f"➡️ Использую найденный файл: {fallback}")
            ref_audio_path = fallback
        else:
            print(f"❌ Файл не найден: {ref_audio_path}")
            print("\nДоступные аудио/видео файлы на рабочем столе:")
            for file in os.listdir(desktop_path):
                if file.endswith((".mov", ".mp4", ".wav", ".mp3", ".m4a")):
                    print(f"  - {file}")
            return

    # Exact transcript of reference audio
    ref_text = "один два три"
    print(f"\nРеференсный текст: {ref_text}")

    # Load model
    print("Загрузка модели Qwen3-TTS-12Hz-0.6B-Base...")
    model = Qwen3TTSModel.from_pretrained(
        "Qwen/Qwen3-TTS-12Hz-0.6B-Base",
        device_map=device,
        dtype=torch.float32,
    )
    print("✅ Модель загружена!")

    # Create prompt from reference audio
    print("Создание промпта для клонирования голоса...")
    voice_clone_prompt = model.create_voice_clone_prompt(
        ref_audio=ref_audio_path,
        ref_text=ref_text,
        x_vector_only_mode=False,
    )
    print("✅ Промпт создан!")

    # Generate output
    target_text = (
        "Привет! Это тест клонирования голоса на русском языке. Сегодня прекрасная погода."
    )
    print(f"Генерация речи: '{target_text}'")
    wavs, sr = model.generate_voice_clone(
        text=target_text,
        language="Russian",
        voice_clone_prompt=voice_clone_prompt,
    )

    output_path = os.path.join(desktop_path, "cloned_voice_output.wav")
    sf.write(output_path, wavs[0], sr)

    print(f"\n✅ Готово! Файл сохранён: {output_path}")
    print(f"Частота дискретизации: {sr} Hz")
    print(f"Длительность: {len(wavs[0]) / sr:.2f} секунд")


if __name__ == "__main__":
    main()

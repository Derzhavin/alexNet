структура диоектории classifier:
    sample/
        bee/
        wasp/
    tables/

    add_paths_for_samples.py
    resize_images.py
    pretrained.py
    data_generator.py
    net.py
    test.py
    tune.py
    use.py

Подготовка изображений:
1) python3 resize_images.py;
2) python3 add_paths_for_samples.py.

Тренировка сети:
1) python3 tune.py.

Проверка сети:
1) python3 test.py

Применение сети:
1) python3 use.py
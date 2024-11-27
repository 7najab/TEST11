from abc import ABC, abstractmethod
from playsound import playsound  # Імпортуємо бібліотеку для відтворення звуку


# Інтерфейс для реалізації будильника
class AlarmCImpl(ABC):
    @abstractmethod
    def ring(self):
        pass

    @abstractmethod
    def notify(self):
        pass

# Конкретна реалізація будильника 1 (Звуковий сигнал)
class SoundAlarm(AlarmCImpl):
    def ring(self):
        print("Будильник дзвонить звуковим сигналом!")
        playsound('alarm_sound.mp3')  # Відтворюємо звуковий файл при дзвінку будильника

    def notify(self):
        print("Повідомлення: Ви прокинулись!")

# Конкретна реалізація будильника 2 (Текстове повідомлення)
class TextAlarm(AlarmCImpl):
    def ring(self):
        print("Будильник дзвонить через текстовий сигнал!")

    def notify(self):
        print("Повідомлення: Час прокидатися!")

# Абстракція для будильника
class AlarmC(ABC):
    def __init__(self, alarm_impl: AlarmCImpl):
        self._alarm_impl = alarm_impl

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def toWake(self):
        pass

# Конкретний будильник 1 (Звичайний будильник)
class StandardAlarm(AlarmC):
    def start(self):
        print("Будильник запущений.")

    def stop(self):
        print("Будильник зупинено.")

    def toWake(self):
        print("Прокидайтесь!")
        self._alarm_impl.ring()
        self._alarm_impl.notify()

# Конкретний будильник 2 (Будильник з вибором сповіщення)
class SmartAlarm(AlarmC):
    def start(self):
        print("Розумний будильник запущений.")

    def stop(self):
        print("Розумний будильник зупинено.")

    def toWake(self):
        print("Прокидайтесь, це ваш розумний будильник!")
        self._alarm_impl.ring()
        self._alarm_impl.notify()

# Тестування
sound_alarm = StandardAlarm(SoundAlarm())  # Використовуємо SoundAlarm для звуку
smart_alarm = SmartAlarm(TextAlarm())

print("Тестування звичайного будильника:")
sound_alarm.start()
sound_alarm.toWake()
sound_alarm.stop()

print("\nТестування розумного будильника:")
smart_alarm.start()
smart_alarm.toWake()
smart_alarm.stop()

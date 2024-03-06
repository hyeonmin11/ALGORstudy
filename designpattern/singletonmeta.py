class SingletonMeta(type):
    """ 
    The Singleton class can be implemented in different ways in Python.
    Some possible methods include base class, decorator, metaclass. 
    We will use the metaclass because it is best suited for this purpose.
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the '__init__' arguement don't affect the returned instance
        """
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        
        return cls._instances[cls]
    
    
class Singleton(metaclass = SingletonMeta):
    def some_business_logic(self):
        print("business logic")

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance")
    else:
        print("Singleton failed, variables contain different instances")

#프로그램 전체에서 단 하나의 인스턴스만 생성한다.
#첫번쨰 인스턴스 생성 요청 시, singletonmeta call method가 새 인스턴스를 생성하고 인스턴스 딕셔너리에 저장한다
#이후 같은 클래스에 대한 인스턴스 생성 요청이 있을 때는 _instance 딕셔너리에 저장된 기존 인스턴스를 반환하여 싱글톤 패턴을 유지한다.

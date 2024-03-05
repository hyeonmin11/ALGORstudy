using System;

namespace RefactoringGuru.Designpatterns.Mediator.Conceptual
{
    public interface IMediator
    {
        void Notify(object sender, string ev);
    }

    //Concrete Mediators implement cooperative behavior by coordinaating several components
    class ConcreteMediator : IMediator
    {
        private Component1 _component1;
        private Component2 _component2;

        public ConcreteMediator(Component1 component1, Component2 component2)
        {
            this._component1 = component1;
            this._component1.SetMediator(this);
            this._component2 = component2;
            this._component2.SetMediator(this);
        }

        public void Notify(object sender, string ev)
        {
            if (ev == "A")
            {
                Console.WriteLine("Mediator reacts on A and triggers following operations:");
                this._component2.DoC();
            }
            if(ev == "D"){
                Console.WriteLine("Mediator reacts on D and triggers following operations:");
                this._component1.DoB();
                this._component2.DoC();
            }
        }
    }


    // The Base Component provides the basic functionality of storing a mediator's instance inside component objects.
    class BaseComponent
    {
        protected IMediator _mediator;
        public BaseComponent(IMediator mediator = null){
            this._mediator = mediator;
        }
        public void SetMediator(IMediator mediator){
            this._mediator = mediator;
        }
    }

    //concrete Components implement various functionality. They don't depend on other components.
    //They also don't depend on any concrete mediator classes
    class Component1 : BaseComponent
    {
        public void DoA(){
            Console.WriteLine("Component 1 does A");
            this._mediator.Notify(this, "A");
        }

        public void DoB(){
            Console.WriteLine("Component 1 does B.");
            this._mediator.Notify(this, "B");
        }
    }
    class Component2 : BaseComponent
    {
        public void DoC()
        {
            Console.WriteLine("Component 2 does C.");
            this._mediator.Notify(this, "C");
        }

        public void DoD()
        {
            Console.WriteLine("Component 2 does D.");
            this._mediator.Notify(this, "D");
        }
    }

    class Program{
        static void Main(string[] args)
        {
            //Client code
            Component1 component1 = new Component1();
            Component2 component2 = new Component2();
            new ConcreteMediator(component1, component2);

            Console.WriteLine("Client triggers operation A.");
            component1.DoA();

            Console.WriteLine();

            Console.WriteLine("Client triggers operation D.");
            component2.DoD();
        }
    }
}
'''
rtrace.trace:

    Decoratore per funzioni ricorsive che ne traccia l'esecuzione,
    gli argomenti e i valori tornati (ed il livello di ricorsione).

Esempio::

    from rtrace import trace
    
    @trace
    def fattoriale(N):
        if N==1:
            return 1
        else:
            return N*fattoriale(N-1)
    
    fattoriale.trace(4)
    ------------------- Starting recursion -------------------
    entering       fattoriale(4,)
    |-- entering    fattoriale(3,)
    |--|-- entering fattoriale(2,)
    |--|--|-- entering      fattoriale(1,)
    |--|--|-- exiting       fattoriale(1,)  returns 1
    |--|-- exiting  fattoriale(2,)  returns 2
    |-- exiting     fattoriale(3,)  returns 6
    exiting        fattoriale(4,)  returns 24
    -------------------- Ending recursion --------------------
    Num calls: 4
        
    fattoriale.count(8)
    Num calls: 8

'''



# TODO: prevedere tracciamento dei metodi di una classe

class TraceRecursion:
    def __init__(self,f):
        "store the function and initialize counter and level"
        self.f = f
        self.traceP = False
        self.countP = False
        self.indent = 0
        self.numcalls = 0

    def count(self,*args,**kargs):
        "just count the calls"
        self.traceP = False
        self.countP = True
        self.numcalls = 0
        answer = self.__call__(*args,**kargs)
        print('Num calls:', self.numcalls)
        self.countP = False
        return answer

    def trace(self,*args,**kargs):
        "trace the calls to the function and their level and return"
        self.traceP = True
        self.countP = True
        self.indent = 0
        self.numcalls = 0
        print('------------------- Starting recursion -------------------')
        # call the decorator
        answer = self.__call__(*args,**kargs)
        print('-------------------- Ending recursion --------------------')
        print('Num calls:', self.numcalls)
        self.countP = False
        self.traceP = False
        return answer

    def __call__(self,*args,**kargs):
        '''Conta e traccia (se richiesto) le chiamate alla funzione'''
        if self.traceP:
            indent     = '|--'*self.indent
            callstring = self.f.__name__
            if args : callstring += str(args)
            if kargs: callstring += str(kargs)
            print (indent+" entering", callstring , sep='\t')
            self.indent += 1
        if self.countP:
            self.numcalls += 1
        # call the decorated function
        answer = self.f(*args,**kargs)
        if self.traceP:
            self.indent -= 1
            print(indent+' exiting ', callstring,"returns", answer, sep='\t')
        return answer

trace = TraceRecursion

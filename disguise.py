import random
import re

# 随机后缀池
randomExtPool=['bin:10','dll:20','pkg:10','dat:5','efi:8','lib:8','wim:5','drv:5','sys:4','pyc:1','img:1','fbx:2','pif:3','cat:1','db:2','ocx:0',':50']
randomNamePool=[
	'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
	'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
	'0','1','2','3','4','5','6','7','8','9',
	'a2a', 'abc', 'abstract', 'abstraction', 'accelerated', 'acceptance', 'access', 'accessible', 'account', 'achieve', 'acquire', 'action', 'activate', 'active', 'activex', 'actual', 'adapter', 'add', 'addition', 'address', 'adimm', 'adjacency', 'adl', 'ado', 'advanced', 'after', 'aggregation', 'agu', 'aha', 'ahead', 'ai', 'aided', 'algorithm', 'alias', 'align', 'allocate', 'allocator', 'alu', 'amr', 'analog', 'analysis', 'analytical', 'and', 'angle', 'annotation', 'api', 'app', 'appearance', 'append', 'application', 'applications', 'architecture', 'archive', 'area', 'argument', 'arithmetic', 'array', 'arrow', 'artificial', 'as', 'asp', 'assembly', 'assert', 'asset', 'assets', 'assign', 'assignment', 'assistant', 'associated', 'associative', 'assume', 'assurance', 'asynchronous', 'atm', 'atomic', 'attribute', 'attributes', 'audio', 'authentication', 'authorization', 'automation', 'aware', 'b2b', 'back', 'background', 'backup', 'backward', 'bait', 'balance', 'balancing', 'ball', 'bandwidth', 'bar', 'base', 'based', 'batch', 'bcl', 'beis', 'beist', 'benchmark', 'benefit', 'best', 'bfs', 'bga', 'bht', 'bild', 'biliti', 'binary', 'binding', 'bit', 'bitmap', 'bits', 'bitwise', 'black', 'block', 'blocked', 'board', 'body', 'bookkeeping', 'boolean', 'border', 'bound', 'boundary', 'bounds', 'box', 'boxing', 'bpu', 'brace', 'brach', 'bracket', 'brakcet', 'branch', 'breadth', 'breakpoint', 'breis', 'bridge', 'broker', 'browser', 'bu', 'bubble', 'buffers', 'bug', 'build', 'built', 'bundle', 'bus', 'business', 'button', 'buttons', 'by', 'byte', 'cable', 'cache', 'calculation', 'calculations', 'calendar', 'call', 'callback', 'calls', 'candidate', 'capability', 'capacity', 'card', 'carrier', 'cartesian', 'cascading', 'case', 'casting', 'catalog', 'ccp', 'cd', 'cell', 'center', 'ceramic', 'chain', 'character', 'characteristic', 'characters', 'chart', 'check', 'checked', 'checking', 'checkpoint', 'child', 'chip', 'chips', 'cil', 'circuit', 'circular', 'cisc', 'class', 'classification', 'clause', 'cleanup', 'cli', 'client', 'clipboard', 'clk', 'clock', 'clone', 'clr', 'cls', 'cluster', 'cmos', 'coaxial', 'cob', 'cod', 'code', 'coded', 'coff', 'cohesion', 'coincidental', 'collection', 'collision', 'coloring', 'column', 'com', 'combination', 'combo', 'command', 'comment', 'commit', 'common', 'communication', 'comparison', 'compatible', 'compilation', 'compile', 'compiler', 'complement', 'complementary', 'complex', 'complexity', 'component', 'composite', 'composition', 'computer', 'computing', 'concept', 'concrete', 'concurrency', 'concurrent', 'condition', 'configuration', 'confirm', 'conform', 'connection', 'connectivity', 'connector', 'consist', 'consistency', 'console', 'const', 'constant', 'constrain', 'constraint', 'constraints', 'construct', 'constructor', 'consumer', 'contain', 'container', 'containment', 'content', 'contention', 'context', 'contract', 'control', 'controller', 'cookie', 'copy', 'corba', 'corporation', 'correspond', 'corresponding', 'counting', 'coupling', 'cover', 'cpett', 'cpga', 'cpi', 'cpu', 'create', 'creation', 'critical', 'crosstab', 'crtp', 'csma', 'ctor', 'cts', 'cube', 'curiously', 'curly', 'cursor', 'custom', 'cycle', 'cyclic', 'cylinder', 'dai', 'data', 'database', 'databases', 'datagram', 'dataset', 'db', 'dbcs', 'dbms', 'dcl', 'dcom', 'ddl', 'dead', 'deadlock', 'deallocate', 'debug', 'debugger', 'debugging', 'decay', 'decimal', 'decision', 'declaration', 'declarative', 'decode', 'decomposition', 'decrease', 'ded', 'deduction', 'default', 'defer', 'defi', 'define', 'definition', 'deit', 'delegate', 'delegation', 'delete', 'deli', 'demarshal', 'demonstrate', 'dependent', 'deploy', 'depth', 'dereference', 'deri', 'derivation', 'derived', 'description', 'design', 'destroy', 'destructor', 'determine', 'developer', 'development', 'device', 'dfs', 'dhtml', 'di', 'diagram', 'dialog', 'dib', 'dictionary', 'die', 'difference', 'digest', 'digital', 'dime', 'dimensional', 'dinl', 'direct', 'directed', 'direction', 'directive', 'directory', 'dirty', 'dis', 'disassembler', 'disco', 'discovery', 'disk', 'dispatch', 'dispid', 'distinguish', 'distributed', 'divide', 'division', 'dju', 'dlectronic', 'dml', 'dna', 'document', 'dom', 'domain', 'dot', 'double', 'dqdb', 'draw', 'dres', 'dri', 'driven', 'driver', 'dsn', 'dtd', 'dtor', 'dual', 'dump', 'dynamic', 'e97afd47a751', 'eai', 'ebco', 'ec', 'edge', 'edi', 'editor', 'effect', 'efficiency', 'efficient', 'ei', 'eit', 'eksikju', 'eksit', 'element', 'elevator', 'embedded', 'empty', 'en', 'enable', 'encapsulation', 'enclosing', 'encode', 'end', 'engine', 'engineering', 'enterprise', 'entites', 'entity', 'entry', 'enum', 'enumeration', 'enumerators', 'environment', 'epic', 'equal', 'equality', 'equation', 'equivalence', 'equivalent', 'error', 'escape', 'estimate', 'estimeit', 'ethernet', 'evaluate', 'evaluation', 'even', 'event', 'evidence', 'evolution', 'exceed', 'excel', 'exception', 'exchange', 'exclusion', 'exclusive', 'executable', 'execute', 'execution', 'executive', 'exhibit', 'existence', 'exit', 'expansion', 'expertise', 'explicit', 'explicitly', 'export', 'expression', 'extensible', 'extensions', 'external', 'facility', 'factory', 'fadd', 'fail', 'fain', 'fainl', 'false', 'fast', 'fat', 'fault', 'faun', 'fcpga', 'fddi', 'fdiv', 'fdm', 'feature', 'feiz', 'femms', 'fetch', 'fft', 'fi', 'fiber', 'fid', 'field', 'fifo', 'figure', 'fiks', 'file', 'filter', 'final', 'finalization', 'finalizer', 'firewall', 'firmware', 'first', 'fit', 'fk', 'flag', 'flash', 'flat', 'fleksi', 'flexibility', 'flip', 'float', 'floating', 'floationg', 'flop', 'floppy', 'flow', 'fluorided', 'flush', 'fmul', 'font', 'for', 'foreign', 'form', 'formal', 'format', 'formula', 'forum', 'forward', 'forwarding', 'foundation', 'fourier', 'fpu', 'fractal', 'fragmentation', 'frame', 'framework', 'frequency', 'fsub', 'ftp', 'ful', 'full', 'function', 'functional', 'functionality', 'functionally', 'functions', 'functor', 'gac', 'game', 'garbage', 'gateway', 'gather', 'gc', 'general', 'generate', 'generation', 'generator', 'generic', 'genericity', 'getter', 'global', 'globally', 'gopher', 'grade', 'grant', 'granularity', 'graph', 'graphic', 'graphical', 'grid', 'group', 'guarantee', 'guard', 'gui', 'guid', 'gvpp', 'hand', 'handle', 'handler', 'handling', 'hard', 'hardware', 'hash', 'hdlc', 'head', 'header', 'heap', 'hed', 'help', 'hertz', 'hi', 'hierarchical', 'hierarchy', 'high', 'hit', 'hl', 'hook', 'host', 'hot', 'html', 'http', 'https', 'hub', 'huk', 'hwait', 'hyperlink', 'hypertext', 'ia', 'icon', 'icu', 'id', 'ide', 'identifier', 'identify', 'idf', 'idl', 'idle', 'ieu', 'if', 'ik', 'iks', 'il', 'ili', 'illinois', 'illustrate', 'im', 'image', 'ime', 'imm', 'immediate', 'immutability', 'immutable', 'implement', 'implementation', 'implicit', 'implimen', 'import', 'in', 'increment', 'incremental', 'indeks', 'independent', 'index', 'indi', 'indication', 'indirect', 'infinite', 'influence', 'information', 'infrastructure', 'inheritance', 'initialization', 'initialize', 'initially', 'inline', 'inner', 'inorder', 'input', 'insertion', 'insi', 'instance', 'instantiated', 'instantiation', 'instruction', 'instructions', 'insulator', 'integer', 'integral', 'integrate', 'integrated', 'integration', 'integrity', 'intel', 'intelligence', 'interacts', 'interchange', 'interconnect', 'interface', 'intermediate', 'internal', 'internet', 'interoperability', 'interpreter', 'interprocess', 'interrupt', 'intersection', 'introspection', 'invalid', 'invariants', 'invoke', 'ion', 'iostream', 'ipc', 'isa', 'isam', 'isolation', 'item', 'iterate', 'iteration', 'iterative', 'iterator', 'itming', 'java', 'jit', 'join', 'ju', 'judgment', 'kaiv', 'katmai', 'keibl', 'kernel', 'kernels', 'key', 'ki', 'kit', 'kju', 'kli', 'kni', 'kri', 'laiftaim', 'lain', 'lan', 'land', 'language', 'large', 'laser', 'late', 'latency', 'layer', 'ld', 'ldt', 'leak', 'left', 'lei', 'lekt', 'length', 'lev', 'level', 'li', 'library', 'lifetime', 'lightning', 'line', 'link', 'linkage', 'linked', 'linker', 'list', 'literal', 'livelock', 'lju', 'load', 'loader', 'local', 'locator', 'lock', 'locking', 'locks', 'log', 'logic', 'logical', 'login', 'long', 'longitudinal', 'look', 'lookup', 'loop', 'loose', 'lt', 'lu', 'lvalue', 'ly', 'machine', 'macro', 'magic', 'mail', 'maintain', 'maintanence', 'man', 'managed', 'management', 'manager', 'managers', 'manchester', 'mangled', 'manifest', 'manipulation', 'manipulator', 'many', 'map', 'markup', 'marshal', 'mart', 'matrix', 'maus', 'md5', 'mechanism', 'mein', 'meitriks', 'member', 'members', 'memberwise', 'memory', 'menju', 'menu', 'mesi', 'message', 'meta', 'metadata', 'metal', 'metaprogramming', 'method', 'metropolitan', 'mflop', 'mflops', 'mhz', 'mi', 'micro', 'middle', 'middleware', 'million', 'millions', 'mimd', 'min', 'minimum', 'mips', 'mis', 'misd', 'miss', 'mit', 'mju', 'mmu', 'mmx', 'mobile', 'mode', 'model', 'modeling', 'modem', 'modified', 'modifier', 'module', 'modules', 'molap', 'monitor', 'most', 'mouse', 'mp', 'mps', 'ms', 'msrs', 'multi', 'multicast', 'multidimensional', 'multilevel', 'multimedia', 'multiple', 'multiplexing', 'multiplication', 'multiprocessor', 'multithreaded', 'multiuser', 'mutable', 'mutex', 'mutual', 'name', 'named', 'namespace', 'naoc', 'native', 'natural', 'nd', 'neimspeis', 'neitiv', 'nerik', 'nested', 'nestid', 'net', 'network', 'new', 'ngen', 'ni', 'nifaid', 'nit', 'nju', 'no', 'noise', 'non', 'nondependent', 'normal', 'ns', 'nt', 'null', 'number', 'numbers', 'nyquist', 'object', 'objects', 'obtain', 'occupy', 'occurrence', 'odbc', 'odd', 'odr', 'ods', 'of', 'olap', 'old', 'ole', 'olga', 'oltp', 'on', 'one', 'online', 'only', 'oodb', 'oom', 'ooo', 'opaque', 'open', 'operand', 'operate', 'operating', 'operation', 'operations', 'operator', 'optic', 'optimization', 'optimized', 'optimizer', 'option', 'optional', 'oracle', 'order', 'ordinary', 'organic', 'organize', 'oriented', 'os', 'out', 'outer', 'output', 'overclock', 'overflow', 'overhead', 'overlapping', 'overload', 'overloaded', 'override', 'owner', 'oxide', 'p250', 'package', 'packaging', 'packet', 'page', 'paged', 'pages', 'pail', 'paip', 'pair', 'palette', 'pane', 'parallel', 'parameter', 'parameterize', 'parent', 'parentheses', 'parse', 'parser', 'part', 'partial', 'party', 'pass', 'passing', 'path', 'pattern', 'pbga', 'pcb', 'pda', 'pe', 'pediction', 'peer', 'peik', 'pein', 'pend', 'per', 'perception', 'perform', 'performance', 'period', 'permit', 'permutate', 'persistence', 'personal', 'pga', 'phase', 'physcal', 'physical', 'pi', 'pib', 'pin', 'pinvoke', 'pipe', 'pipeline', 'pixel', 'pju', 'pk', 'place', 'placeholder', 'placement', 'plain', 'plastic', 'platform', 'platter', 'pleksiti', 'plisit', 'plugin', 'plugins', 'pod', 'poi', 'point', 'pointer', 'policy', 'polish', 'poll', 'polymorphism', 'pooling', 'pop', 'port', 'portability', 'portable', 'post', 'postfix', 'postorder', 'powerpoint', 'ppga', 'pqfp', 'pr', 'prai', 'praim', 'precedence', 'predicate', 'prediction', 'predikeit', 'preemption', 'prefix', 'preorder', 'preprocessor', 'presentation', 'pressure', 'pri', 'primary', 'prime', 'primer', 'primitiv', 'primitive', 'principle', 'print', 'printer', 'priority', 'procedural', 'procedure', 'procedures', 'process', 'processing', 'processor', 'product', 'proficient', 'profile', 'profiler', 'program', 'programmer', 'programming', 'programs', 'progress', 'project', 'projection', 'property', 'proposition', 'protocal', 'protocol', 'prototype', 'prototyping', 'provider', 'pseudo', 'psju', 'psn', 'pump', 'punctuation', 'purose', 'purpose', 'quad', 'qualified', 'qualifier', 'quality', 'query', 'queue', 'queuing', 'race', 'radian', 'radio', 'raid', 'raise', 'raivd', 'random', 'range', 'rank', 'rate', 'ratio', 'raw', 're', 'read', 'readonly', 'ready', 'real', 'record', 'recordset', 'recovery', 'recurring', 'recursive', 'redirected', 'redo', 'reduced', 'redundancy', 'redundency', 'ref', 'refactoring', 'refer', 'reference', 'referential', 'referred', 'reflection', 'refresh', 'regard', 'register', 'registers', 'registry', 'regular', 'regularly', 'rei', 'reit', 'reiz', 'rekt', 'rektid', 'rektiv', 'relation', 'relational', 'relationship', 'relay', 'reliability', 'remark', 'remote', 'renaming', 'repeater', 'replacement', 'replication', 'represent', 'repri', 'request', 'requirements', 'resolution', 'resolve', 'resource', 'response', 'restory', 'restriction', 'result', 'retirement', 'retrieve', 'return', 'revoke', 'ri', 'rientid', 'right', 'ring', 'risc', 'riser', 'ristik', 'robust', 'robustness', 'role', 'roll', 'rollback', 'root', 'router', 'routine', 'row', 'rowset', 'rpc', 'ru', 'rule', 'rules', 'running', 'runtime', 'rvalue', 'safe', 'saikl', 'saiklik', 'sain', 'save', 'savepoint', 'sax', 'scalable', 'scan', 'schedule', 'scheduler', 'schema', 'scheme', 'scope', 'screen', 'script', 'scroll', 'scrubbing', 'sdk', 'sealed', 'search', 'sec', 'second', 'sector', 'security', 'see', 'seek', 'segments', 'seif', 'sel', 'select', 'selection', 'semantics', 'semaphore', 'semaphores', 'semi', 'semiconductor', 'sequence', 'sequential', 'serial', 'serialization', 'serialize', 'series', 'server', 'service', 'services', 'session', 'set', 'setter', 'setting', 'settings', 'sha1', 'shaking', 'shallow', 'shanon', 'share', 'shared', 'short', 'shortest', 'si', 'sibling', 'side', 'signal', 'signature', 'silicon', 'siliti', 'sim', 'simd', 'similar', 'simple', 'sin', 'single', 'sio2f', 'sisd', 'sist', 'siv', 'sju', 'sk', 'skeip', 'ski', 'sklu', 'skri', 'slider', 'slot', 'smart', 'smds', 'smi', 'smm', 'smp', 'smtp', 'snapshot', 'soap', 'sof', 'software', 'soi', 'solution', 'solve', 'sonc', 'sort', 'sound', 'source', 'space', 'spanning', 'spec', 'specialization', 'specializations', 'specific', 'specification', 'specify', 'speculative', 'speedup', 'spend', 'spesifi', 'spi', 'splisit', 'splitter', 'sql', 'sqrt', 'square', 'sse', 'sstf', 'st', 'stack', 'stails', 'standard', 'starvation', 'state', 'stateless', 'statement', 'statements', 'static', 'status', 'stl', 'storage', 'store', 'stored', 'strategy', 'stream', 'streaming', 'strein', 'streint', 'stri', 'stribjutid', 'strict', 'strikt', 'string', 'structure', 'structured', 'stub', 'styles', 'stylesheet', 'subclass', 'subgroup', 'subobject', 'subquery', 'subroutine', 'subscript', 'subset', 'subtraction', 'subtype', 'superclass', 'superscalar', 'supervisor', 'support', 'suppose', 'suspend', 'switch', 'switching', 'symbol', 'symbolic', 'symmetric', 'syntax', 'synthetic', 'system', 'systolic', 'table', 'tables', 'tag', 'taim', 'taip', 'tape', 'target', 'task', 'tasking', 'tcp', 'tdm', 'technology', 'teibl', 'tein', 'tek', 'tekst', 'temp', 'template', 'templit', 'temporary', 'term', 'terminal', 'testing', 'text', 'theta', 'thin', 'third', 'thread', 'threaded', 'through', 'throughput', 'throw', 'ti', 'tier', 'time', 'timestamping', 'tisi', 'tist', 'tju', 'tlb', 'to', 'token', 'toy', 'trace', 'track', 'transaction', 'transactional', 'transfer', 'transform', 'transformation', 'translate', 'translation', 'transmit', 'transparent', 'transport', 'traversal', 'traverse', 'tree', 'trench', 'tribju', 'trigger', 'triggers', 'tuple', 'two', 'type', 'types', 'uddi', 'uml', 'unary', 'unboxing', 'uncacheabled', 'unchecked', 'underflow', 'undirected', 'unified', 'uniform', 'union', 'unique', 'unit', 'units', 'universary', 'universe', 'unmanaged', 'unmarshal', 'unqualified', 'unwinding', 'up', 'update', 'updating', 'upload', 'uri', 'url', 'user', 'using', 'uswc', 'utils', 'vaid', 'vais', 'valu', 'value', 'variable', 'vector', 'vee', 'vendor', 'vent', 'vertical', 'vertice', 'very', 'via', 'viable', 'video', 'view', 'virtual', 'visual', 'vliw', 'volatile', 'vowel', 'vpu', 'vsam', 'waid', 'wait', 'waiz', 'wan', 'warehouse', 'waterfall', 'web', 'weit', 'where', 'white', 'wide', 'wildcard', 'window', 'windows', 'wizard', 'word', 'worker', 'world', 'wrapper', 'write', 'wsdl', 'www', 'xmi', 'xml', 'xsd', 'xsl', 'xslt', 'zain', 'zekjutiv', 'zent', 'zibit'
]

def randomExt():
	randomExtList=[]
	for ext in randomExtPool:
		extSplit=ext.split(':')
		e=extSplit[0]
		w=1
		if len(extSplit)==2:
			w=int(extSplit[1])
		for i in range(0,w):
			randomExtList.append(e)
	return random.choice(randomExtList)

def randomName():
	randomNameList=[]
	for name in randomNamePool:
		nameSplit=name.split(':')
		n=nameSplit[0]
		w=1
		if len(nameSplit)==2:
			w=int(nameSplit[1])
		for i in range(0,w):
			randomNameList.append(n)
	return random.choice(randomNameList)

def nameSplice(nl):
	nameSp=''
	for i,name in enumerate(nl):
		if i==0:
			nameSp+=name
		else:
			nameSp+=name.capitalize()
	return nameSp

def is_alphanumeric(input_str):
	pattern = r'^[a-zA-Z0-9]+$'
	match = re.match(pattern, input_str)
	if match:    
		return True
	else:    
		return False

randomSelectNameAlready=[]
def randomSelectName():
	wCount=random.randint(1,3)
	nameList=[]
	for i in range(0, wCount):
		nameList.append(random.choice(randomNamePool))
	nameFinally=nameSplice(nameList)
	if len(nameFinally)<2 or nameFinally in randomSelectNameAlready: # 文件名长度小于2，或存在于已用池中，则重随
		nameFinally=randomSelectName()
	randomSelectNameAlready.append(nameFinally)
	return nameFinally

numberSelectNameIndex=0
def numberSelectName():
	global numberSelectNameIndex
	numStr=f'{numberSelectNameIndex}'
	numberSelectNameIndex+=1
	return numStr

charSelectNameIndex=0
def charSelectName():
	global charSelectNameIndex
	charStr=f'{decTo26(charSelectNameIndex)}'
	charSelectNameIndex+=1
	return charStr.lower()

sequence = list( map( lambda x: chr( x ), range( ord( 'A' ), ord( 'Z' ) + 1 ) ) )
def decTo26(num):
	d, m = divmod(num,26) # 26 is the number of ASCII letters
	return '' if num < 0 else decTo26(d-1)+chr(m+65) # chr(65) = 'A'
	# global sequence
	# L = []
	# num=num-1;  #实现从1对应A
	# if num > 25:
	# 	while True:
	# 		d = int( num / 26 )
	# 		remainder = num % 26
	# 		if d <= 25:
	# 			L.insert( 0, sequence[remainder] )
	# 			L.insert( 0, sequence[d - 1] )
	# 			break
	# 		else:
	# 			L.insert( 0, sequence[remainder] )
	# 			num = d - 1
	# else:
	# 	L.append( sequence[num] )
	# return "".join( L )


if __name__=='__main__':
	# for i in range(0,1000):
	# 	print(randomSelectName())
	# return
	f=open('words.txt','rb')
	l=[
		# '\'a\'','\'b\'','\'c\'','\'d\'','\'e\'','\'f\'','\'g\'','\'h\'','\'i\'','\'j\'','\'k\'','\'l\'','\'m\'','\'n\'','\'o\'','\'p\'','\'q\'','\'r\'','\'s\'','\'t\'','\'u\'','\'v\'','\'w\'','\'x\'','\'y\'','\'z\'',
		# '\'A\'','\'B\'','\'C\'','\'D\'','\'E\'','\'F\'','\'G\'','\'H\'','\'I\'','\'J\'','\'K\'','\'L\'','\'M\'','\'N\'','\'O\'','\'P\'','\'Q\'','\'R\'','\'S\'','\'T\'','\'U\'','\'V\'','\'W\'','\'X\'','\'Y\'','\'Z\'',
		# '\'0\'','\'1\'','\'2\'','\'3\'','\'4\'','\'5\'','\'6\'','\'7\'','\'8\'','\'9\''
	]
	a=f.read().decode(encoding='utf-8').split('\r\n')
	f.close()
	for i in a:
		s=i.lower()
		if is_alphanumeric(i) and len(i)>1:
			l.append(f'\'{s}\'')
	l=list(set(l)) #去重
	l.sort()
	f=open('words1.txt','w')
	f.write(', '.join(l))
	f.close()
	input('PAUSE')

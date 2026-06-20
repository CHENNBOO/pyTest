# Java 转 Python 对比总结

> 面向有 Java 经验的开发者，梳理两门语言的核心差异与思维转换

---

## 1. 数据结构对比

Python 中同样提供了内置数据结构，对应 Java 的集合框架，且作为语言级"第一公民"直接可用。

### 1.1 对应关系

| Python | Java | 特点 |
|--------|------|------|
| `list` | `List` (ArrayList) | 有序可重复，支持混合类型，无需泛型 |
| `dict` | `Map` (HashMap) | 键值对，API 响应直接转 dict，无需 POJO |
| `set` | `Set` (HashSet) | 无序唯一，原生支持 `&` `\|` `-` 集合运算 |
| `tuple` | 无直接对应 | 有序不可变，保证数据不被篡改 |
| `list`（模拟栈） | `Stack` | `append()` 入栈，`pop()` 出栈 |
| `collections.deque` | `Queue` | 双端队列 |

### 1.2 创建示例

```python
# list — 无需泛型，可混合类型
my_list = ["apple", "banana", 123]

# dict — 无需定义 POJO 类
user = {"name": "Alice", "age": 25}

# set — 原生支持集合运算
tags = {"python", "java"}

# tuple — 不可变序列
point = (10, 20)
```

### 1.3 字面量坑点

| 写法 | 类型 | 说明 |
|------|------|------|
| `{1, 2, 3}` | `set` | 只有值，没有冒号 |
| `{"a": 1, "b": 2}` | `dict` | 键值对，冒号连接 |
| `{}` | `dict`（空字典） | ⚠️ 默认是空字典，不是空集合！ |
| `set()` | `set`（空集合） | 创建空集合必须用 `set()` |

---

## 2. 语法与代码结构

### 2.1 直观差异

| 维度 | Java | Python |
|------|------|--------|
| 代码块 | `{}` 大括号 | **缩进**（4空格） |
| 语句结束 | `;` 分号 | 换行即结束 |
| 变量声明 | `String name = "Alice";` | `name = "Alice"` |
| 常量 | `final` / `const` | 约定全大写 `MAX_SIZE = 100` |
| 字符串拼接 | `"Hi " + name` | `f"Hi {name}"`（f-string） |

### 2.2 函数定义

```java
// Java
public int add(int a, int b) {
    return a + b;
}
```

```python
# Python
def add(a, b):
    return a + b
```

> 不需要返回值类型、参数类型，不需要 `{}` 和 `;`

### 2.3 类定义

```java
// Java
public class Dog {
    private String name;

    public Dog(String name) {
        this.name = name;
    }

    public void sayHi() {
        System.out.println("Hi, I am " + this.name);
    }
}
```

```python
# Python
class Dog:
    def __init__(self, name):      # __init__ = 构造函数
        self.name = name

    def say_hi(self):               # self = this，但必须显式写出
        print(f"Hi, I am {self.name}")
```

> 要点：`self` 必须写在方法参数第一位，但调用时不用传；构造方法是 `__init__`。

### 2.4 访问修饰符

| Java | Python | 说明 |
|------|--------|------|
| `public` | `name` | 公开，直接访问 |
| `protected` | `_name` | 约定受保护（单下划线），只是约定 |
| `private` | `__name` | 名称改写（双下划线），解释器改了名字 |

> Python 没有真正的 private，"我们都是成年人"。

### 2.5 Python 独有的解包语法

```python
# 变量交换（不需要临时变量）
a, b = b, a

# 多重赋值
x, y, z = 1, 2, 3

# 函数返回多个值
def get_coord():
    return 10, 20
x, y = get_coord()
```

---

## 3. 控制流与异常

| 维度 | Java | Python |
|------|------|--------|
| 条件分支 | `if / else if / else` | `if / elif / else` |
| 一行 if | `x > 0 ? x : -x` | `x if x > 0 else -x` |
| for 循环 | `for (int i=0; i<n; i++)` | `for i in range(n):` |
| 异常捕获 | `try-catch-finally` | `try-except-finally` |
| 抛出异常 | `throw new Exception()` | `raise Exception()` |
| 包管理 | `import` + Maven/Gradle | `import` + pip |

```python
# Python 一行 if-else（三元运算符）
age_status = "成年" if age >= 18 else "未成年"

# Python for 循环 — 直接遍历对象，不需要索引
for item in my_list:
    print(item)

# 需要索引时用 enumerate
for i, item in enumerate(my_list):
    print(i, item)
```

---

## 4. 鸭子类型（Duck Typing）⭐ 核心差异

### 4.1 Java 的做法：先看"身份证"（接口）

```java
// 必须先定义接口
interface ISpeakable {
    void speak();
}

// 类必须声明实现接口
class Dog implements ISpeakable {
    public void speak() { System.out.println("汪汪"); }
}

class Cat implements ISpeakable {
    public void speak() { System.out.println("喵喵"); }
}

// 参数必须是 ISpeakable 类型
public void makeItSpeak(ISpeakable animal) {
    animal.speak();  // 编译器检查：有 speak() 吗？有！放行！
}
```

### 4.2 Python 的做法：只看"行为"

```python
class Dog:
    def speak(self):
        print("汪汪")

class Cat:
    def speak(self):
        print("喵喵")

# 不需要任何接口！
def make_it_speak(animal):
    animal.speak()  # 运行时才检查：有 speak() 就执行，没有才报错
```

### 4.3 连"动物"都不是也能用

```python
class Robot:
    def speak(self):
        print("滴答滴答，我是机器人")

make_it_speak(Robot())  # 完全合法！有 speak() 就是"鸭子"
```

### 4.4 思维差异总结

| | Java（静态类型） | Python（鸭子类型） |
|---|---|---|
| 检查时机 | **编译期** | **运行期** |
| 约束方式 | 接口 / 继承 | 只要有对应方法 |
| 优点 | 安全，IDE 提示强 | 灵活，样板代码极少 |
| 缺点 | 接口/抽象类写得多 | 传错对象运行时才报错 |

> **一句话**：Java 里你先证明自己是鸭子才能下水；Python 里你直接下水，能嘎嘎叫就是鸭子。

---

## 5. 列表推导式 — 一行替代 Stream API

### 5.1 基本映射（map）

```java
// Java Stream
list.stream().map(x -> x * 2).collect(Collectors.toList())
```

```python
# Python
[x * 2 for x in list]
```

### 5.2 过滤 + 映射（filter + map）

```java
// Java
list.stream()
    .filter(x -> x % 2 == 0)
    .map(x -> x * x)
    .collect(Collectors.toList())
```

```python
# Python — 一行
[x * x for x in list if x % 2 == 0]
```

### 5.3 展平（flatMap）

```java
// Java
matrix.stream()
    .flatMap(row -> row.stream())
    .collect(Collectors.toList())
```

```python
# Python
[col for row in matrix for col in row]
```

### 5.4 更多示例

```python
# 字符转 ASCII
[ord(c) for c in "FishC"]              # [70, 105, 115, 104, 67]

# 提取矩阵某列
[row[1] for row in matrix]              # [2, 5, 8]

# 笛卡尔积
[x + y for x in "ab" for y in "12"]    # ['a1','a2','b1','b2']

# 嵌套条件
[[x, y] for x in range(10) if x % 2 == 0
        for y in range(10) if y % 3 == 0]
```

---

## 6. 上下文管理器（with 语句）— 替代 try-with-resources

```java
// Java try-with-resources
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String line = br.readLine();
    System.out.println(line);
}  // 自动关闭
```

```python
# Python with 语句 — 更简洁
with open("file.txt") as f:
    line = f.readline()
    print(line)
# 自动关闭，即使发生异常也会关闭
```

> `with` 是 Python 的上下文管理器协议，任何实现了 `__enter__` / `__exit__` 的对象都可以用 `with`。

---

## 7. 生成器（yield）— Python 独有的惰性迭代

```java
// Java：一次性生成所有数据，返回 List
public List<Integer> getNumbers() {
    List<Integer> result = new ArrayList<>();
    for (int i = 0; i < 1000000; i++) {
        result.add(i);
    }
    return result;  // 100万个整数全部加载到内存
}
```

```python
# Python：惰性生成，用多少取多少
def get_numbers():
    for i in range(1000000):
        yield i    # 每次只产出一个值，不占内存

for num in get_numbers():
    if num > 10:
        break      # 只生成前 11 个，后面的根本不计算
```

> `yield` 让函数变成生成器，只在需要时计算下一个值，适合处理大数据流。

---

## 8. 装饰器（@decorator）— 比 Java 注解更强大

```python
# 装饰器是一个函数，用来包装另一个函数
def log_time(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} 耗时 {time.time() - start:.2f}s")
        return result
    return wrapper

@log_time  # 一行就给函数加上计时功能
def slow_function():
    sum(range(10000000))

slow_function()
# 输出: slow_function 耗时 0.35s
```

> Java 注解是元数据，需要框架（如 Spring AOP）解析才能生效；Python 装饰器本身就是可执行代码，直接包装函数。

---

## 9. 其他核心编程思维差异

| 维度 | Java | Python |
|------|------|--------|
| 一切皆对象 | 基本类型（int, boolean）不是对象 | 函数、类、模块、数字都是对象 |
| 类型系统 | 编译时强类型 | 运行时动态类型 |
| main 方法 | 必须有 `public static void main` | 代码从上往下直接执行 |
| 迭代 | Stream API | `for ... in` + `yield` 生成器 |
| 设计模式 | 工厂/策略/观察者... | 字典映射/高阶函数就能解决 |

---

## 10. 高频场景速查

| 场景 | Java | Python |
|------|------|--------|
| 遍历列表 | `for (String s : list)` | `for s in list:` |
| 带索引遍历 | `for (int i=0; i<list.size(); i++)` | `for i, item in enumerate(list):` |
| 遍历字典 | `for (Map.Entry e : map.entrySet())` | `for k, v in dict.items():` |
| 检查包含 | `list.contains(x)` | `x in list` |
| 字符串格式化 | `String.format("Hi %s", name)` | `f"Hi {name}"` |
| 空值检查 | `obj == null` | `obj is None` |
| 类型检查 | `obj instanceof Dog` | `isinstance(obj, Dog)` |
| 获取类名 | `obj.getClass().getSimpleName()` | `type(obj).__name__` |
| 三目运算 | `x > 0 ? x : -x` | `x if x > 0 else -x` |

---

## 11. 给 Java 转 Python 的建议

1. **放下类型焦虑**：不要总想给变量加类型注解。Python 3.5+ 支持 Type Hints（如 `def add(a: int, b: int) -> int:`），但只为 IDE 提示，运行时不管
2. **拥抱 Pythonic**：多写列表推导式、用 `with` 管理资源、尝试 `yield` 生成器
3. **不要过度设计**：一个字典映射就能替代简单工厂，一个函数就能替代策略模式
4. **利用 REPL**：Python 交互式解释器是探索 API 的利器，Java 没有这个体验
5. **读优秀开源代码**：Requests、Flask、FastAPI 的源码是 Pythonic 典范

---

## 12. 相同点（让你感到亲切）

| 维度 | 说明 |
|------|------|
| 面向对象 | 类、对象、封装、继承、多态 |
| 数据结构概念 | List / Dict / Set 概念完全一致 |
| 控制流关键字 | if / else / for / while / break / continue |
| 异常处理 | try-except-finally ≈ try-catch-finally |
| 包管理 | import + pip ≈ import + Maven/Gradle |

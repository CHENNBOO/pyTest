# Java 转 Python 对比总结

> 面向有 Java 经验的开发者，梳理两门语言的核心差异

---

## 1. 数据结构对比

Python 中同样提供了内置数据结构，对应 Java 的集合框架，且作为语言级"第一公民"直接可用。

| Python | Java | 特点 |
|--------|------|------|
| `list` | `List` (ArrayList) | 有序可重复，支持混合类型，无需泛型 |
| `dict` | `Map` (HashMap) | 键值对，API 响应直接转 dict，无需 POJO |
| `set` | `Set` (HashSet) | 无序唯一，原生支持 `&` `\|` `-` 集合运算 |
| `tuple` | 无直接对应 | 有序不可变，保证数据不被篡改 |
| `list`（模拟栈） | `Stack` | `append()` 入栈，`pop()` 出栈 |
| `collections.deque` | `Queue` | 双端队列 |

**创建示例：**

```python
my_list = ["apple", "banana", 123]          # list
user = {"name": "Alice", "age": 25}          # dict
tags = {"python", "java"}                    # set
point = (10, 20)                             # tuple
```

**字面量区分：**

| 写法 | 类型 | 说明 |
|------|------|------|
| `{1, 2, 3}` | `set` | 只有值，没有冒号 |
| `{"a": 1, "b": 2}` | `dict` | 键值对，冒号连接 |
| `{}` | `dict`（空字典） | ⚠️ 默认是空字典，不是空集合 |

---

## 2. 语法与代码结构

### 2.1 直观差异

| 维度 | Java | Python |
|------|------|--------|
| 代码块 | `{}` 大括号 | **缩进**（4空格） |
| 语句结束 | `;` 分号 | 换行即结束 |
| 变量声明 | `String name = "Alice";` | `name = "Alice"` |
| 常量 | `final` / `const` | 约定全大写 `MAX_SIZE = 100` |

### 2.2 函数定义

```python
# Java:  public int add(int a, int b) { return a + b; }
# Python:
def add(a, b):
    return a + b
```

### 2.3 self vs this

```python
class Dog:
    def say_hi(self):              # self = Java 的 this
        print(f"Hi, {self.name}")  # 调用时不需要传 self
```

### 2.4 访问修饰符

| Java | Python | 说明 |
|------|--------|------|
| `public` | `name` | 公开 |
| `protected` | `_name` | 约定受保护（单下划线） |
| `private` | `__name` | 名称改写（双下划线） |

> Python 崇尚"我们都是成年人"，没有真正的私有。

---

## 3. 控制流与异常

| 维度 | Java | Python |
|------|------|--------|
| 条件分支 | `if / else if / else` | `if / elif / else` |
| 循环 | `for / while` | `for / while` |
| 异常 | `try-catch-finally` | `try-except-finally` |
| 抛出异常 | `throw` | `raise` |
| 包管理 | `import` + Maven/Gradle | `import` + pip |

---

## 4. 鸭子类型（Duck Typing）⭐ 核心差异

### 4.1 Java 的做法：先看"身份证"（接口）

```java
// 必须定义接口
interface ISpeakable {
    void speak();
}

// 类必须实现接口
class Dog implements ISpeakable {
    public void speak() { System.out.println("汪汪"); }
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
    animal.speak()  # 运行时才检查：有 speak() 吗？有就执行
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
| 约束方式 | 接口/继承 | 只要方法存在 |
| 优点 | 安全，IDE 提示好 | 灵活，代码少 |
| 缺点 | 样板代码多 | 传错对象运行才报错 |

> **一句话**：Java 里你必须先证明自己是鸭子才能下水；Python 里你直接下水，能嘎嘎叫就承认你是鸭子，淹死了才报错。

---

## 5. 列表推导式 — Python 的"表达力核武器"

一行代码完成 Java 中 Stream API 的过滤、映射、聚合：

```python
# Java: list.stream().filter(x -> x%2==0).map(x -> x*x).collect(Collectors.toList())
# Python:
[x*x for x in nums if x % 2 == 0]
```

---

## 6. 其他核心编程思维差异

| 维度 | Java | Python |
|------|------|--------|
| 一切皆对象 | 基本类型不是对象 | 函数、类、模块都是对象 |
| 类型系统 | 强类型，必须声明 | 动态类型，直接赋值 |
| 迭代思维 | Stream API | 迭代器协议 + `yield` 生成器 |
| 设计模式 | 工厂/策略等 | 字典映射/高阶函数即可 |
| 运行方式 | 编译→字节码→JVM | 解释型，直接运行源码 |

---

## 7. 给 Java 转 Python 的建议

1. **放下类型焦虑**：不要总想给变量加类型注解，Python 类型提示只是 IDE 辅助，运行时不管
2. **拥抱 Pythonic**：学习列表推导式、`with` 语句、装饰器 `@` 等 Python 独有写法
3. **不要过度设计**：一个字典映射就能解决的问题，不需要工厂模式

---

## 8. 相同点（让你感到亲切）

| 维度 | 说明 |
|------|------|
| 面向对象 | 类、对象、封装、继承、多态 |
| 数据结构 | List / Dict / Set 概念一致 |
| 控制流 | if / else / for / while / break / continue |
| 异常处理 | try-except-finally ≈ try-catch-finally |
| 包管理 | import + pip ≈ import + Maven |

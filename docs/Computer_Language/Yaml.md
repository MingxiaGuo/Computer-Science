# YAML

YAML：YAML Ain’t Markup Language (YAML™) ，

Offical website: https://yaml.org/

Docs: https://yaml.org/spec/1.2.2/

### yaml格式

- 以.yml格式为后缀
- 键值对使用冒号结构表示 key: value，冒号后面要加一个空格

### yaml的基本语法

- 大小写敏感
- 使用缩进表示层级关系
- 缩进不允许使用tab，只允许空格
- 缩进的空格数不重要，只要相同层级的元素左对齐即可
- '#'表示注释

### yaml的数据类型

- 对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
- 数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
- 纯量（scalars）：单个的、不可再分的最基本的值





yq

有时需要将json和yaml格式的配置文件进行相互转换，那么在linux的环境下，yq就是一个很好的命令行的工具。
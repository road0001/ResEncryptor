# 资源加密压缩工具

##### 一个简易但强大的资源加密压缩工具。

本工具旨在尽可能减轻资源压缩、分享和解压的心智负担，无须多层压缩，无须设置过于复杂的密码，一切从简，仅靠拖放、双击、输入密码即可完成一切操作。复杂的操作，交给计算机就好！

## 使用方法

### 加密压缩：

1. 从dist或release中下载最新版本ResEncryptor.exe。
2. 拖放你想加密压缩的文件或文件夹到此exe上。
3. 设定一个密码，并写一段留言。
4. 等待加密压缩完成。
5. 分享时必须包括目录下的所有文件！

### 解密解压：

1. 双击目录下的exe文件。
2. 输入解压密码。
3. 等待解压完成。
4. 根据需要决定是否删除压缩包和exe文件。
5. Enjoy！

## 扩展阅读

### 加密、压缩算法：

- 当用户将文件或文件夹拖放到exe图标上时，将开始扫描此文件或文件夹，获取文件数和总大小。
- 根据总大小，随机生成分卷数量，计算得到分卷大小，并加上随机增量。
  - 注：由于7Z存在一定压缩比，因此此处计算的分卷数量仅供参考。
- 根据用户输入的密码、随机盐、当前时间戳，生成一个长达128位含大小写字母、数字的密码，有效避免各种暴力破解。
- 将上述随机盐、当前时间戳等数据保存到解密配置中，并根据不同情况，随机生成混淆数据。
- 根据用户输入的密码，加密配置文件。
- 调用7Z命令行工具，根据密码、分卷大小开始压缩，压缩包放在输出目录。压缩过程中同时加密文件名，避免任何明文暴露。
- 等待压缩完成。
- 遍历生成的文件，使用规则中的随机字符串重命名并将映射关系保存到解密配置中。
- 根据用户输入的密码，计算解密配置的密钥和IV。
- 使用上述密钥和IV，用AES加密配置数据。
- 随机生成32位解密配置文件名并将加密后的数据写入文件。
- 将解密EXE复制到输出目录。
- 将解密配置文件、解密文件名按顺序写入EXE文件的末尾。
- 清理掉不需要的临时文件。
- 加密操作完成。

### 解密、解压算法：

- EXE运行时，读取自身末尾32位字节，获取解密配置文件名。
- 查找并读取解密配置文件，询问用户密码。
  - 如果未找到，程序将询问用户配置文件名。
- 根据用户输入的密码解密配置数据，从中获取到随机盐、时间戳和文件名映射关系。
- 根据映射关系将文件重命名回正确名称。
- 根据用户输入的密码、随机盐、当前时间戳，生成128位密码。
- 调用7Z命令行工具，使用上述密码进行解压，解压后的文件输出到当前目录。
- 清理掉不需要的临时文件。
- 解密操作完成。

### 关于混淆：

- 混淆是为了避免通过大数据、DPI探测等方式识别出加密内容而在数据中加盐的一种方法。比如在生成加密数据时，其内容和KEY顺序大体上不会发生变化，因此在加密后，哪怕用不同的密钥和IV，信息熵的分布仍然与原始数据接近，这就令DPI识别有了用武之地，通过大量数据训练，最终能够精准识别这类数据。
- 本工具在多处使用了混淆。在生成解密配置数据时，会插入多段随机生成的字符串，并将所有的KEY进行乱序处理，使得有价值的信息熵降低，这样在进行AES加密后，就很难被机器扫描、识别出它的作用。
- 在进行加密压缩时，会对其进行分卷处理，分卷大小根据文件大小、随机分卷数量和随机增量决定。在完成压缩后，会将所有压缩包的文件名更改成随机字符串，这样在上传、分享时其排序是乱的，很难精准定位到文件头。而其他文件由于分卷大小不同，其内容也是完全不同的，其对应的MD5也是完全不同，从而降低被精准识别的概率。
- 与此同时，也在Python代码中随机加入了数条随机生成的字符串，并且每个版本都会对其进行更换。虽然这会影响生成的文件体积并略微降低性能，但也可以有效降低有价值内容被识别的概率。
- 在生成EXE时，由于前面的Python代码中加入了混淆数据，因此每个版本生成的EXE文件也会有很大的不同。就算使用同一个版本的EXE文件，在每次进行加密压缩时，都会在其尾部添加解密配置数据以及解密配置文件，从而使得每次生成的EXE文件MD5均不相同，有效降低文件被识别的概率。

## 高级用法

本工具使用Python开发，因此您需要配置Python开发环境，安装依赖，才可进行开发和修改。 

- 从官网下载安装Python 3。

- Python版本不低于3.11。

- 使用PIP安装下面的依赖。

  - ```shell
    pip install send2trash
    pip install pycryptodomex
    pip install pyinstaller
    ```

  - 您也可以双击install.bat自动安装依赖。

- 根据自己的需求修改源码。

- 使用pyinstaller将源码打包成EXE可执行文件。

  - ```shell
    pyinstaller -F ResEncryptor.py
    // 如果想要自定义图标，可使用下方的命令：
    pyinstaller -F -i icon.ico ResEncryptor.py
    ```

  - 您也可以双击“build.bat”自动进行打包。
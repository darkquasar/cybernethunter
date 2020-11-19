# Author: Diego Perez
# Version: 0.1

Function ConvertTo-GZipCompressedByteArray {

    <#

    .SYNOPSIS
        Function to convert a file or string to a compressed byte array.

    .DESCRIPTION
        Function to convert a file or string to a compressed byte array. It will return a byte array representing the compressed object.

    .PARAMETER StringToCompress
        A string that you would like to compress using GZip

    .PARAMETER ByteArrayToCompress
        The DN of the base directory to search from.

    .PARAMETER ObjectToCompress
        The object that requires compression: a string, a byte array or a file. In any case all non-byte array objects are converted to byte arrays.

    .EXAMPLE
        Todo

    #>

    Param (
        [Parameter(ValueFromPipeline=$True,ValueFromPipelineByPropertyName=$True)]
        [String]$StringToCompress,

        [Parameter(Mandatory=$False)]
        [byte[]]$ByteArrayToCompress,

        [Parameter(Mandatory=$False)]
        [String]$FilePath,

        [Parameter(Mandatory=$True)]
        [ValidateSet("string", "file", "bytearray")]
        [String]$ObjectToCompress

    )
    
    # Setting this at the beginning of any function to determine whether we should be providing output to stdout
    # Useful for debugging.
    if ($PSBoundParameters['Verbose']) { $Global:LogfileWriteConsole = $True } elseif ($Global:LogfileWriteConsole -ne $True) { $Global:LogfileWriteConsole = $False }

    ### Configure GZip Stream
    [System.IO.MemoryStream]$CompressedMemStream = [System.IO.MemoryStream]::new()
    $GZipCompressionStream = [System.IO.Compression.GZipStream]::new($CompressedMemStream, ([System.IO.Compression.CompressionMode]::Compress))

    switch ($ObjectToCompress) {

        string { 
            [System.Text.Encoding] $StringEncoder = [System.Text.Encoding]::UTF8
            [byte[]] $EncodedString = $StringEncoder.GetBytes( $StringToCompress )

            ### COMPRESS
            $GZipCompressionStream.Write($EncodedString, 0, $EncodedString.Length)
            $GZipCompressionStream.Close()
            $CompressedMemStream.Close()
            
            return $CompressedMemStream.ToArray()
         }

        file { 
            $FileBytes = [IO.File]::ReadAllBytes($FilePath)

            ### COMPRESS
            $GZipCompressionStream.Write($FileBytes, 0, $FileBytes.Length)
            $GZipCompressionStream.Close()
            $CompressedMemStream.Close()
            
            return $CompressedMemStream.ToArray()
        }

        bytearray {
            ### COMPRESS
            $GZipCompressionStream.Write($ByteArrayToCompress, 0, $ByteArrayToCompress.Length)
            $GZipCompressionStream.Close()
            $CompressedMemStream.Close()
            
            return $CompressedMemStream.ToArray()
        }

    }

}

Function ConvertFrom-GZipCompressedByteArray {

    <#

    .SYNOPSIS
        Function to convert a file or string back to its original byte representation from a compressed byte array.

    .DESCRIPTION
        Function to convert a file or string back to its original byte representation from a compressed byte array. It will return a byte array representing the decompressed object.

    .PARAMETER CompressedByteArray
        A string that you would like to compress using GZip

    .EXAMPLE
        Todo

    #>

    Param (
        [Parameter(ValueFromPipeline=$True,ValueFromPipelineByPropertyName=$True)]
        [String]$StringToCompress,

        [Parameter(Mandatory=$False)]
        [byte[]]$ByteArrayToCompress,

        [Parameter(Mandatory=$False)]
        [String]$FilePath,

        [Parameter(Mandatory=$False)]
        [ValidateSet("string", "file", "bytearray")]
        [String]$ObjectToCompress

    )
    
    # Setting this at the beginning of any function to determine whether we should be providing output to stdout
    # Useful for debugging.
    if ($PSBoundParameters['Verbose']) { $Global:LogfileWriteConsole = $True } elseif ($Global:LogfileWriteConsole -ne $True) { $Global:LogfileWriteConsole = $False }

    ### Configure GZip Stream
    [System.IO.MemoryStream]$CompressedMemStream = [System.IO.MemoryStream]::new()
    $GZipCompressionStream = [System.IO.Compression.GZipStream]::new($CompressedMemStream, ([System.IO.Compression.CompressionMode]::Compress))

    ### DECOMPRESS
    $Input = New-Object System.IO.MemoryStream( , $CompressedMemStream.ToArray() )
    $DecompressedMemStream = [System.IO.MemoryStream]::new()
    #$DecompressedMemStream = [System.IO.File]::Create("mierda3.txt")
    $GZipDecompressionStream = [System.IO.Compression.GZipStream]::new($Input, [System.IO.Compression.CompressionMode]::Decompress)
    $GZipDecompressionStream.CopyTo($DecompressedMemStream)
    Write-Output "Decompressed Stream:", $DecompressedMemStream

    switch ($ObjectToCompress) {

        string { 
            [System.Text.Encoding] $StringEncoder = [System.Text.Encoding]::UTF8
            [byte[]] $EncodedString = $StringEncoder.GetBytes($StringToCompress)

            ### COMPRESS
            $GZipCompressionStream.Write($EncodedString, 0, $EncodedString.Length)
            $GZipCompressionStream.Close()
            $CompressedMemStream.Close()
            
            return $CompressedMemStream.ToArray()
         }

        file { 
            $FileBytes = [IO.File]::ReadAllBytes($FilePath)

            ### COMPRESS
            $GZipCompressionStream.Write($FileBytes, 0, $FileBytes.Length)
            $GZipCompressionStream.Close()
            $CompressedMemStream.Close()
            
            return $CompressedMemStream.ToArray()
        }

        bytearray {
            ### COMPRESS
            $GZipCompressionStream.Write($ByteArrayToCompress, 0, $ByteArrayToCompress.Length)
            $GZipCompressionStream.Close()
            $CompressedMemStream.Close()
            
            return $CompressedMemStream.ToArray()
        }

    }

}

Function Convert-ByteArrayToString {

    <#

    .SYNOPSIS
        Function to convert a byte array to its string representation.


    .PARAMETER ByteArray
        The byte array you wish to convert

    .EXAMPLE
        Todo

    #>

    Param (
        [Parameter(ValueFromPipeline=$True,ValueFromPipelineByPropertyName=$True)]
        [byte[]]$ByteArray

    )
    
    # Setting this at the beginning of any function to determine whether we should be providing output to stdout
    # Useful for debugging.
    if ($PSBoundParameters['Verbose']) { $Global:LogfileWriteConsole = $True } elseif ($Global:LogfileWriteConsole -ne $True) { $Global:LogfileWriteConsole = $False }

    [System.Text.Encoding] $StringEncoder = [System.Text.Encoding]::UTF8
    $StringEncoder.GetString( $ByteArray ) | Out-String

}


<#
Example Importing PoshSSH From Memory

$poshsshdll = [Convert]::ToBase64String([IO.File]::ReadAllBytes("C:\Downloads\PoshSSH.dll"))
$rencisshdll = [Convert]::ToBase64String([IO.File]::ReadAllBytes("C:\Downloads\Renci.SshNet.dll"))

$ByteArrayPoshSSHDLL = [System.Convert]::FromBase64String($poshsshdll)
$PoshSSHInMemoryAssembly = [System.Reflection.Assembly]::Load($ByteArrayPoshSSHDLL)

$ByteArrayRenciSSHDLL = [System.Convert]::FromBase64String($rencisshdll)
$RenciSSHInMemoryAssembly = [System.Reflection.Assembly]::Load($ByteArrayRenciSSHDLL)

Import-Module -Assembly $ByteArrayPoshSSHDLL
Import-Module -Assembly $RenciSSHInMemoryAssembly

#>
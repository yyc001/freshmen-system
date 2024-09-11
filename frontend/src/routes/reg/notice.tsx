import { createFileRoute } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { Alert, Button, Input } from 'antd'
import { useState } from 'react'

export const Route = createFileRoute('/reg/notice')({
  loader: async (params : any) => {
    console.log(params)
  },
  component: () => {
    const [promiseValue, setPromiseValue] = useState('');
    const [isDisabled, setisDisabled] = useState(false);
    const [showConfirm, setShowConfirm] = useState(false);
    const iAgreeText = '我已阅读并同意上述内容';

    return (
      <>
      <PageContent>
        <h1> 报名 · 承诺</h1>
        <Alert
            message="我承诺："
            description={<>
                <p>我已仔细阅读泰山学堂学生选拔工作通知中的每一个字，我将认真阅读报名系统中的提示文字，认真仔细完成信息填报。</p>
                <p>我是报考学生本人，我不是考生的家长或同学，我将自己独立填写所有报名信息。</p>
                <p>我报名和考试期间所填报的各类信息真实、准确、有效，不提供任何虚假、错误信息。</p>
                <p>我严格遵守《山东大学本科考试考生守则》以及其他相关法律和考试纪律，诚信考试，不违规、不作弊。</p>
                <p>我严格遵守考试的保密要求，在选拔各阶段不拍照、录音、录像、直播、录屏、投屏，在选拔结果公示结束前不以任何形式透露传播试题内容等有关情况。</p>
                <p>我报考前慎重考虑，不中途退考或缺考，进入学堂后两周内不退出学堂。</p>
                <p>如违反上述承诺，本人自行承担由此造成的一切后果。</p>
                </>}
            type="info"
            showIcon
        />
        <p onDragStart={(e: any) => {e.preventDefault()}} onDrop={(e: any) => {e.preventDefault()}}>
            请在文本框内输入 <code>{iAgreeText}</code>以继续。
        </p>
        <Input
            type="text"
            // name="promise"
            value={promiseValue}
            onChange={(e: any) => {
                const value = e.target.value;
                setPromiseValue(value);
                setShowConfirm(value === iAgreeText);
            }}
            onPaste={(e : any) => {
                e.preventDefault();
                setPromiseValue('不要耍小聪明');
                setisDisabled(true);
            }}
            disabled={isDisabled}
            autoComplete="off"
        />
        {
        showConfirm && 
            <Button href='/reg/basic-info?notice=1' type="primary" >{iAgreeText}</Button>
        }
      </PageContent>
      </>
    )
  },
})
